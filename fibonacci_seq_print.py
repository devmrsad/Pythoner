try:
    max = int(input("The maximum for fibonacci sequence: "))
except ValueError:
    exit("You should enter a number!")

if max < 1 or max > 100:
    exit("Unsupported value!")

string = ["-"] * max
fib_numbers = []

a, b = 1, 2
while a <= max:
    fib_numbers.append(a)
    a, b = b, a + b


for j in range(len(string)):
    item_to_look_for = j + 1
    if item_to_look_for in fib_numbers:
        string[j] = "+"

print(''.join(string))