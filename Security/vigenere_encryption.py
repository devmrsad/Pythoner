def operation(text, keysText, action):
    result = []
    if not keysText or not text or (action != "e" and action != "d"):
        exit("Warning: Bad input!")
    keysText = keysText.upper()

    key_num = 0
    for char in text:
        if char.isalpha():
            starting_index = 65 if char.isupper() else 97
            # the ascii of the key char
            key_order = ord(keysText[key_num]) - ord("A")
            # the ascii of the current char
            char_order = ord(char) - starting_index
            sum_order = None
            # encryption case
            if action == "e":
                sum_order = (char_order + key_order) % 26
            # decryption case
            else:
                sum_order = (char_order - key_order) % 26
            
            sum_order %= 26
            char = chr(starting_index + sum_order)

            key_num = (key_num + 1) % len(keysText)
        
        result.append(char)
    
    return "".join(result)

def vigenere_encryption(text = "", keysText = "key"):
    return operation(text, keysText, "e")

def vigenere_decryption(text = "", keysText = "key"):
    return operation(text, keysText, "d")

key = "key"
encrypted = vigenere_encryption("Mohammadreza", key)
decrypted = vigenere_decryption(encrypted, key)

print(f"The text {decrypted} will be encrypted to {encrypted} with the key \"{key}\"")