from math import ceil
def enc(text = "random text", key = "test"):
    grid = [[] for _ in range( ceil(len(text) / len(key)) )]
    text_arr = list(text)

    for i in range(len(grid)):
        part_to_append = text_arr[:len(key)]
        if(len(part_to_append) < len(key)):
            part_to_append += ["X"] * (len(key) - len(part_to_append))
        grid[i] = part_to_append
        if(len(text_arr) > len(key)):
            text_arr = text_arr[(len(key)):]
    
    key_arr = list(key)
    pairs = [(i, key_arr[i]) for i in range(len(key_arr))]
    pairs.sort(key=lambda x: (x[1], x[0]))
    order = [i for i, _ in pairs]

    res = []
    for col in order:
        for row in grid:
            res.append(row[col])

    return "".join(res)

def dec(cipher="random text", key="test"):
    rows = ceil(len(cipher) / len(key))
    order = sorted(range(len(key)), key=lambda i: key[i])

    full_cols = len(cipher) % len(key) or len(key)

    parts, start = {}, 0
    for i in order:
        length = rows if i < full_cols else rows - 1
        parts[i] = cipher[start:start+length]
        start += length

    output = "".join(parts[c][r] for r in range(rows) for c in range(len(key)) if r < len(parts[c]))
    return output.rstrip("X")

encryption_key = "encrypt"

encrypted = enc("Text to be encrypted", encryption_key)
decrypted = dec(encrypted, encryption_key)

print(f"Main text:\n{decrypted}")
print(f"Encrypted text:\n{encrypted}")