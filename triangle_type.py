print("YOU WILL ENTER THREE SIDE LENGTHS TO FIND OUT IF THEY COULD SHAPE A TRIANGLE")

try:
    a = int(input("The first side length: "))
    b = int(input("The second side length: "))
    c = int(input("The third side length: "))
except Exception as e:
    exit(f"Error: {e}")

if a <= 0 or b <= 0 or c <= 0:
    exit("All of the side lengths should be more than 0!")

# final check
if a < b + c and b < a + c and c < a + b:
    # it is triangle. Let's find the type
    print("Congrats! These sizes can shape a triangle!")
    if a == b == c:
        print("It's a equilateral triangle.")
    elif a == b or a == c or b == c:
        print("It's a isosceles triangle.")
    else:
        print("It's a scalene triangle.")
    
    sides_list = sorted([a, b, c])
    if sides_list[0] ** 2 + sides_list[1] ** 2 == sides_list[2] ** 2:
        print("And it's also a right triangle!")
else:
    exit("These are not dimensions of a triangle!")