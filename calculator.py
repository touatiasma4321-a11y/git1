def operation(nb1, nb2, op):
    match op:
        case "+":
            return nb1 + nb2
        case "-":
            return nb1 - nb2
        case "*":
            return nb1 * nb2
        case "/":
            if nb2 == 0:
                return "Error: لا يمكن القسمة على صفر!"
            else:
                return nb1 / nb2
        case "%":
            return nb1 % nb2
        case "**":
            return nb1 ** nb2
        case _:
            return "Error: عملية غير معروفة!"

while True:
    ch = input("entre your operation + - * /  % ** q ")
    if ch == "q":
        print("Exiting the calculator...")
        break
    try:
       nb1 = float(input("Enter the first number:   "))
       nb2 = float(input("Enter the second number:   "))
       print("The result is:", operation(nb1, nb2, ch))
    except ValueError :
       print("Error: please input a valid number!")