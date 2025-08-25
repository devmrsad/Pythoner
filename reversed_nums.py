nums = []
for i in range(1000):
    try:
        num = int(input("Enter a num (0 to terminate): "))
    except ValueError:
        continue
    if num == 0:
        break
    nums.append(num)

nums.reverse()

for num in nums:
    print(num)