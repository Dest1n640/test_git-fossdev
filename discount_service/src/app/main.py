from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import redis.asyncio as redis
from .settings import get_settings

app = FastAPI(title="Discount Service")
settings = get_settings()

# Подключаемся к Redis
redis_client = redis.from_url(settings.redis_url, decode_responses=True)

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    discount_amount: float
    reason: str

@app.on_event("startup")
async def startup_event():
    # Имитация: при старте сервиса заносим промокод STUDENT10 в Redis
    try:
        await redis_client.set("promo:STUDENT10", "10")
    except Exception:
        pass # Если Redis недоступен локально, игнорируем

@app.get("/health")
def health():
    return {"status": "ok", "service": "discount-service"}

@app.post("/discounts/calculate", response_model=DiscountResponse)
async def calculate_discount(request: DiscountRequest):
    discount_percent = 0.0
    reason = "No discount applied"

    # 1. Проверяем промокод через Redis
    if request.promo_code:
        try:
            promo_value = await redis_client.get(f"promo:{request.promo_code}")
            if promo_value:
                discount_percent = float(promo_value)
                reason = f"Promo code '{request.promo_code}' applied"
        except redis.ConnectionError:
            # Если Redis упал, работаем без него (by-design)
            pass

    # 2. Правило оптовой закупки (сработает, если нет промокода или он не найден)
    if discount_percent == 0.0 and request.quantity >= 10:
        discount_percent = 5.0
        reason = "Wholesale discount applied (>= 10 items)"

    # Считаем сумму скидки
    total_price = request.unit_price * request.quantity
    discount_amount = total_price * (discount_percent / 100.0)

    return DiscountResponse(
        discount_percent=discount_percent,
        discount_amount=discount_amount,
        reason=reason
    )
