try:
    init_num = int(input("Enter a number: "))
except ValueError:
    exit("You should enter a number!")

num = init_num

if num <= 1:
    exit("Could not start iterating from this number.")

step = 0
while num != 1:
    step += 1
    num = 3 * num + 1 if num % 2 else num // 2

print(f"It took {step} step(s) to reach 1 from {init_num}.")