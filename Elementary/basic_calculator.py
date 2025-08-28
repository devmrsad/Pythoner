print("Choose a number:\n", "1 -> sum\n", "2 -> min\n", "3 -> div\n", "4 -> mpy\n")
try:
    operation = int(input("Type here: "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    exit("You should choose by entering a number!")

result_txt = "The result "
match(operation):
    case 1:
        result_txt += str(num1 + num2)
    case 2:
        result_txt += str(num1 - num2)
    case 3:
        result_txt += str(num1 // num2)
    case 4:
        result_txt += str(num1 * num2)

print(result_txt)