import pytest
from tax.income import tax_calculator

def test_tax_calculator():
  assert tax_calculator(100) == 13.0
  assert tax_calculator(10.5) == 1.36

@pytest.mark.parametrize("income, expected", [
  (100, 13.0), (10.5, 1.36)
])

def test_calculate_tax_parametrized(income, expected):
  assert tax_calculator(income) == expected

if __name__ == "__main__":
  test_tax_calculator()
  test_calculate_tax_parametrized()
