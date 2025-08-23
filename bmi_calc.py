try:
    weight = int(input("Enter your body weight: "))
    height = int(input("Enter your height in cm: ")) / 100
except:
    exit("The entered values are not numbers!")

# bad input detection
if weight < 15 or weight > 150:
    exit("unsupported weight!")
if height < 1 or height > 2.5:
    exit("unsupported height!")

bmi = round(weight / height ** 2, 2)

print(f"Your bmi is: {bmi}")