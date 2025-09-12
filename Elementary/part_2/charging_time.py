from os import system
try:
    system("cls")
    k = int(input("The battery level is 0 now. How much do you want it to be? "))
except ValueError:
    exit("You should enter a number!")

if k < 1 or k > 100:
    exit("The percentage should be between 1 and 100!")

sum = 0
for i in range(1, k + 1):
    sum = i ** 2 - sum

print(f"It will take {sum} second(s) to be charged {k}%.")