from art import logo

#add
def add(n1, n2):
  return n1 + n2

#subtract
def sub(n1, n2):
  return n1 - n2

#multiply
def mul(n1, n2):
  return n1 * n2

#divide
def div(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div,
}

def calculator():
  print(logo)

  num1 = float(input("Give first number?\n"))
  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation from above: ")
    num2 = float(input("Give second number?\n"))
    cal_function = operations[operation_symbol]
    answer = cal_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}: OR 'n' for new calculation:\n") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()

