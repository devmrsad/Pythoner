# the two first digits of a number have been reversed. So we have to remake the initial number
try:
    temp_num = int(input("Enter the number (3 digits at least): "))
except ValueError:
    exit("You should enter a number!")

if temp_num < 100:
    exit(f"The minimum number is 100! Your number: {temp_num}")

a = temp_num % 10
temp_num //= 10
b = temp_num % 10
temp_num //= 10
new_num = int(str(temp_num) + str(a) + str(b))

print(f"The real number must've been {new_num}")