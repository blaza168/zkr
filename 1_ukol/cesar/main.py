# Data od: https://www.sttmedia.com/characterfrequency-czech
freqs = {
    'a': 0.0720,
    'b': 0.0217,
    'c': 0.0228,
    'd': 0.0373,
    'e': 0.0841,
    'f': 0.0023,
    'g': 0.0026,
    'h': 0.0233,
    'i': 0.0401,
    'j': 0.023,
    'k': 0.0355,
    'l': 0.0516,
    'm': 0.0328,
    'n': 0.0635,
    'o': 0.0796,
    'p': 0.0316,
    'q': 0.0001,
    'r': 0.0340,
    's': 0.0449,
    't': 0.0572,
    'u': 0.0267,
    'v': 0.0394,
    'w': 0.0006,
    'x': 0.0009,
    'y': 0.0241,
    'z': 0.0185,
}

def score(s):
    score = 0
    for char in s:
        c = char.lower()
        if c in freqs:
            score += freqs[c]
    return score

cipher_text = "ctdexhjyx sdbprx jzdan knegprdkpkpb yt hpbdhipict"

CHARS="abcdefghijklmnopqrstuvwxyz"

max_i = 0
max_score = 0
text = ""

for i in range(1,20):
    new_text = ""
    for char in cipher_text:
        position = CHARS.find(char)
        new_position = position - i
        if new_position < 0:
            new_position += len(CHARS)
        new_text += CHARS[new_position]
    text_score = score(new_text)
    if text_score > max_score:
        max_score = text_score
        text = new_text
        max_i = i

print("Max i: " + str(max_i) + " score: " + str(max_score))
print(text)