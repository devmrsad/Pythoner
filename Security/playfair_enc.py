def create_playfair_table(key):
    # creating dict to remove the repetitive characters 
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    table = []
    used = set(key)
    for ch in key:
        if ch.isalpha():
            table.append(ch)
    # the char "J" gets excluded as it will be replaced with "I"
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used: 
            table.append(ch)
            used.add(ch)
    
    return [table[i*5 : (i+1) * 5] for i in range(5)]

def playfair_prepare(txt):
    t = [c for c in txt.upper() if c.isalpha()]
    t = ["I" if c == "J" else c for c in t]
    res, i = [], 0
    
    while i < len(t):
        a = t[i]
        b = t[i+1] if i+1 < len(t) else "X"
        if a == b:
            res.append((a, "X"))
            i += 1
        else:
            res.append((a, b))
            i += 2
        if len(res[-1]) == 1: res[-1] = (res[-1][0], "X")
    return res

def find_pos(table, ch):
    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j
    return None

def playfair_enc(text = "HELLO", key = "playfair encryption"):
    table = create_playfair_table(key)
    pairs = playfair_prepare(text)
    output = []

    for a, b in pairs:
        ai, aj = find_pos(table, a)
        bi, bj = find_pos(table, b)

        if ai == bi:
            output.append(table[ai][(aj + 1) % 5])
            output.append(table[bi][(bj + 1) % 5])
        elif aj == bj:
            output.append(table[(ai + 1) % 5][aj])
            output.append(table[(bi + 1) % 5][bj])
        else:
            output.append(table[ai][bj])
            output.append(table[bi][aj])
    return "".join(output)


# *** USAGE:
print(playfair_enc(text="Text to encrypt", key="Your Special Key"))