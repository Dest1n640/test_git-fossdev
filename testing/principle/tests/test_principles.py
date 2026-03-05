# TODO make if with with pip install -e . math_demo

from math_demo import (add, add_with_bug, tax_calculator_bugged, tax_calculator)

def test_addition():
  assert add(2, 2) == 4
  assert add(0, 0) == 0
  assert add(7, 6) == 13
  print("Test ADDITION PASSED")

def test_addition_with_bug():
  # Тесты показывают наличие ошибок, а не их отсуствие
  assert add_with_bug(2, 2) == 4
  assert add_with_bug(0, 0) == 0
  # assert add_with_bug(7, 6) == 13 # Вызовиться ошибка
  print("Test BUGGED ADDITION PASSED")

def test_addition_duplicate():
  # Тесты не предсказывают работу проверяемой функции
  assert add(6, 7) == 6 + 7
  print("Test DUPLICATE ADDITION PASSED")

def test_addition_overkill():
  for i in range(0, 2 ** 32):
    for j in range(0, 2 ** 32):
      assert add(i, j) == i + j #violation of duplication
      assert add(-i, j) == -i + j
      assert add(-i, -j) == -i - j
      assert add(i, -j) == i - j
  print("Test OVERKILL ADDITION PASSED")


def test_addition_clussters():
  assert add(7, 6) == 13
  assert add(0, 6) == 6
  assert add(7, 0) == 7
  assert add(-7, -6) == -13
  assert add(-1, 0) == -1
  print("Test CLUSSTERS PASSED")

def test_addition_commutative():
  assert add(9, 5) == 14
  assert add(5, 9) == 14
  print("Test COMMUTATIVE PASSED")

def test_tax_calculator():
  assert tax_calculator_bugged(1000) == 150
  assert tax_calculator_bugged(100) == 15
  assert tax_calculator_bugged(10) == 1.5
  assert tax_calculator_bugged(1) == 0.15
  assert tax_calculator_bugged(234) == 35.1
  assert tax_calculator(1000) == 150
  assert tax_calculator(100) == 15
  assert tax_calculator(10) == 1.5
  assert tax_calculator(1) == 0.15
  assert tax_calculator(234) == 35.1
  assert tax_calculator(2.34) == 0.35
  print("Test TAX CALCULATOR")
#  assert tax_calculator_bugged(2.34) == 0.35 # 0.351 # Error


if __name__ == "__main__":
  test_addition()
  test_addition_with_bug()
  test_addition_duplicate()
#  test_addition_overkill()
  test_addition_clussters()
  test_addition_commutative()
  test_tax_calculator()
