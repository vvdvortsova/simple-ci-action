

class MyMath:
  def multiply(a, b):
    return a * b
  
  def sum(a, b):
    return a + b

  def fibonacci(n):
    return fibonacci(n)

def fibonacci(n):
  if n <= 2:
    return 1
  
  return fibonacci(n - 1) + fibonacci(n - 2)
