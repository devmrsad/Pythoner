def enc(text = "Hello World", rails = 3):
    fence = [[] for _ in range(rails)]
    [rail, direction] = [0, 1]
    for ch in text:
        fence[rail].append(ch)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return "".join("".join(row) for row in fence)

def dec(cipher = enc("hello World"), rails = 3):
    fence = [[] for _ in range(rails)]
    pattern = list(range(rails)) + list(range(rails-2, 0, -1))
    [indexes, i] = [[], 0]
    while len(indexes) < len(cipher):
        indexes.append(pattern[i % len(pattern)])
        i += 1
    for rail in range(rails):
        count = indexes.count(rail)
        fence[rail] = list(cipher[:count])
        cipher = cipher[count:]
    res = []
    pos = [0] * rails
    for r in indexes:
        res.append(fence[r][pos[r]])
        pos[r] += 1
    return "".join(res)

print(dec())