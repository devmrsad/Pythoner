try:
    nth_wanted = int(input("Enter the nth number you wanna take: "))
except:
    exit("You should enter a number!")

if nth_wanted < 1:
    exit("Unsupported number.")

index = nth_wanted - 1
nums = []

i = 0
while len(nums) - 1 < index:
    i += 1
    for char in str(i):
        nums.append(char)
        if len(nums) - 1 == index:
            print(f"At position {nth_wanted}, the value is {nums[index]}")
            break