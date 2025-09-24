def multiply_matrices(a, b):
    first_item = (a[0][0] * b[0] + a[0][1] * b[1]) % 26
    second_item = (a[1][0] * b[0] + a[1][1] * b[1]) % 26
    return [ first_item , second_item ]

def text_to_nums(txt):
    nums = [ord(c) - 65 for c in txt.upper() if c.isalpha()]
    return nums

def nums_to_text(nums):
    txt = [chr(n + 65) for n in nums]
    return "".join(txt)

def hill_encrypt(txt, key):
    nums = text_to_nums(txt)
    if len(nums) % 2:
        nums.append(ord("X") - 65)
    
    output = []
    for i in range(0, len(nums), 2):
        vector = [nums[i], nums[i + 1]]
        multiplied = multiply_matrices(key, vector)
        output.extend(multiplied)
    
    return nums_to_text(output)


print(hill_encrypt("hi there", [[19, 8],[9, 25]]))