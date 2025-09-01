def cesar_encrypt(text = "", key = 3):
    result = []
    if not text:
        return False
    
    for char in text:
        if "A"<= char <="Z":
            result.append(chr((ord(char) - 65 + key) % 26 + 65))
        elif "a"<= char <="z":
            result.append(chr((ord(char) - 97 + key) % 26 + 97))
        else:
            result.append(char)

    return "".join(result)

def cesar_decipher(text = "", key = 3):
    return cesar_encrypt(text, -key)

# app interface
print("Characters' encryption app (Using ancient Cesar way)")
txt = input("Enter the text you wanna encrypt: ")

if not cesar_encrypt(txt):
    exit("Bad input")

print("the encrypted text: ", cesar_encrypt(txt))