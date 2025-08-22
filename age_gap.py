selfAge = int(input("please enter your age "))
fathersAge = int(input("please enter your father's age "))

gap = abs(fathersAge - selfAge)

print(f"your father is {gap} years older than you!")

fathersFutureAge = int(input("How old will you be when you wanna know your father's age? ")) + gap
print(f"when you are {fathersFutureAge - gap} years old, your father will be {fathersFutureAge}.")