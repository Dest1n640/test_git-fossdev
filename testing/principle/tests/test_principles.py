# TODO make if with with pip install -e . math_demo
from math_demo import add

def test_addition():
  assert 2 + 2 == 4
  print("Test ADDITION PASSED")

  if __name__ == "__main__":
    test_addition()
