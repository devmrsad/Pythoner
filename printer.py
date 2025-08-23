char = input("Enter a character to print: ")
if len(char) != 1:
    exit("You should input one character!")

try:
    num = int(input("Enter the count of the initial print: "))
except Exception as e:
    exit(f"An error occurred: {e}")

if num < 1:
    exit("The Entered number should be 1 or higher")

print(num * char)
print(num * 2 * char)
print(num * 4 * char)
print(num * 8 * char)