def print_horizontal_side(char, side):
    print(char * side)

def print_vertical_sides(char, side, height):
    for _ in range(height - 2):
        print(char + ' ' * (side - 2) + char)

# input
char = input("Enter a custom character: ")

if len(char) != 1:
    exit("You should input one character!")

try:
    side = int(input("Enter the length of the rectangle side (2 or higher): "))
except Exception as e:
    exit(f"An error occurred: {e}")

if side < 2 or side > 20:
    exit("The side length is either too long or too short!")

# printing the output
print_horizontal_side(char, side)
print_vertical_sides(char, side, 8)
print_horizontal_side(char, side)