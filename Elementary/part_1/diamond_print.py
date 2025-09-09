try:
    a = int(input("Enter a number: "))
except ValueError:
    exit("You should Enter a number!")

if a > 10 or a < 1:
    exit("Unsupported range or number!")

thickness = 1
base = 2 * a + 1

while thickness != base:
    whitespaces_each_side = (base - thickness) // 2
    print(f"{whitespaces_each_side * " "}{thickness * "*"}{whitespaces_each_side * " "}")
    thickness += 2

print(thickness * "*")
thickness -= 2

while thickness >= 1:
    whitespaces_each_side = (base - thickness) // 2
    print(f"{whitespaces_each_side * " "}{thickness * "*"}{whitespaces_each_side * " "}")
    thickness -= 2