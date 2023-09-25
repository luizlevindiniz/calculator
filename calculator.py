import functools

operands = ["+", "-", "*", "/", "^", "r"]

isReading: bool = True

while isReading:
    print("Choose operand:")
    print(*operands, sep=",")
    print("Or type 0 to quit...")
    op = input()

    if op == "0":
        isReading = False

    elif op not in operands:
        print("Invalid Operand!\n")

    else:
        if op == "+":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                print(sum(numbers))
            except:
                print("Invalid entries!")
        elif op == "-":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                result = functools.reduce(lambda x, y: x - y, numbers)
                print(result)
            except:
                print("Invalid entries!")
        elif op == "*":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                result = functools.reduce(lambda x, y: x * y, numbers)
                print(result)
            except:
                print("Invalid entries!")
        elif op == "/":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                result = functools.reduce(lambda x, y: x / y, numbers)
                print(result)
            except:
                print("Invalid entries!")
        elif op == "^":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                result = functools.reduce(lambda x, y: pow(x, y), numbers)
                print(result)
            except:
                print("Invalid entries!")
        elif op == "r":
            try:
                numbers = list(map(int, input("Enter values sep by space: ").split()))
                result = functools.reduce(lambda x, y: x ** (1 / y), numbers)
                print(result)
            except:
                print("Invalid entries!")
        else:
            print("Invalid Operand!\n")
print("Bye!")
