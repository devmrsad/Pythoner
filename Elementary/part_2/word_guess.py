key = input("What will the answer be? ").lower()
tries_count = None
output_list = []

def check_words(key, user_input):
    key_chars_list = list(key)
    input_chars_list = list(user_input)

    for i in range(len(input_chars_list)):
        if(input_chars_list[i] == key_chars_list[i]):
            input_chars_list[i] = "G"
    
    for i in range(len(input_chars_list)):
        for j in range(len(key_chars_list)):
            if input_chars_list[i] == key_chars_list[j]:
                input_chars_list[i] = "Y"
                key_chars_list[j] = "used"

    input_chars_list = list(map(lambda item: "R" if item not in ["G", "Y"] else item, input_chars_list))

    return "".join(input_chars_list).upper()




while True:
    tries_count = input("How many times will the user be able to try? ")
    if tries_count.isnumeric():
        tries_count = int(tries_count)
        break
    print("You should enter a number!")

for i in range(tries_count):
    user_guess = input(f"Guess number {i + 1}: ").lower()

    if i > 0 and output_list[-1] == "G" * len(key):
        output_list.append("Game Over")
        continue
    
    if len(user_guess) != len(key):
        output_list.append("Invalid length")
        continue
    
    output_list.append(check_words(key, user_guess))

for item in output_list:
    print(item)