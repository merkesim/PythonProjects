from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculation():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for operation in operations:
    print(operation)

  choice = True
  while choice:
    symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calc_function = operations[symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to fresh start: ") == 'y':
      num1 = answer
    else:
      choice = False
      calculation()

calculation()
