num1 = float(input("Enter first number: "))
operator = input("Enter operator(+, -, *, /,%, **, //,): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}") 

    case "-":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    case "*":
        result = num1 + num2
        print(f"{num1} * {num2} = {result}")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

    case "%":
        if num2 == 0:
            print("You can't divide by zero")
        else:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")

    case "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")

    case "//":
        if num2 ==0:
            print("You cant divide by zero")

        else:
            result = num1 // num2
            print(f"{num1} // {num2} = {result}")


       