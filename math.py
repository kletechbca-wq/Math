try:
  a = float(input("Enter first number:"))
  b = float(input("Enter second number:"))
  print(f"Addition: {a+b}")
  print(f"Subtraction:{a-b}")
  print("Division by zero is not allowed.")
except valueError:
  print("Please enter valid number.")
