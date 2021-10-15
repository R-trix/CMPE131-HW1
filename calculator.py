def calculator(number1, number2, operator):
    '''
    This function acts as a calculator function, doing basic arithmetic given from the parameters.
    '''
    a = number1
    b = number2
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            return False
        return a / b
    if operator == "//":
        if b == 0:
            return False
        return a // b
    if operator == "**":
        return a ** b
    return False
    
def parse_input():
    '''
    This function takes in the user input and parses it by numbers and operation.
    Once it has been parsed, it then calls the calculator() function to do the calculation.
    '''
    inp = input("Enter equation: ")
    
    inp_list = inp.split()
    num1 = float(inp_list[0])
    op = inp_list[1]
    num2 = float(inp_list[2])
    
    print(calculator(num1, num2, op))