from math import ceil

try:
    first_val , second_val = map(int, input("enter your two values of side length in M with a space between: ").split())
except Exception:
    exit("error reading input values")

# bad input detection
if not first_val or not second_val:
    exit("wrong input detected! exitting the app...")
elif first_val < 0 or second_val < 0:
    exit("negative numbers are not allowed. exitting the app...")

length_cm = max(first_val, second_val) * 100
width_cm = min(first_val, second_val) * 100

ground_area = length_cm * width_cm
tile_area = 4 * 5

needed_titles_count = ceil(ground_area / tile_area)

print(f"you will need {needed_titles_count} tiles at least")