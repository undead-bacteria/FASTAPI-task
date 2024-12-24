import pytest

def perimeter(length, breadth):
  if not length or not breadth:
    raise Exception("Undefined")
  
  if not isinstance(length, (int, float)):
    raise Exception("Not a number")
  
  if not isinstance(breadth, (int, float)):
    raise Exception("Not a number")
  
  if length < 0 or breadth < 0:
    raise Exception("Dimension cannot be negative")
  
  return 2 * (length + breadth)

def test_perimeter_undefined():
  with pytest.raises(Exception, match="Undefined"):
    perimeter(None, 5)
  with pytest.raises(Exception, match="Undefined"):
    perimeter(5, None)

def test_perimeter_negative_dimension():
  with pytest.raises(Exception, match="Dimension cannot be negative"):
    perimeter(-5, 5)
  with pytest.raises(Exception, match="Dimension cannot be negative"):
    perimeter(5, -5)

def test_perimeter_valid_input():
  assert perimeter(5, 10) == 30
  assert perimeter(3.5, 2.5) == 12
  assert perimeter(0, 0) == 0