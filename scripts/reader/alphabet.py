import string
alphabet = string.ascii_lowercase

msg = str(2221202202181405)

for i in range(0, len(msg), 2):
    letter = int(msg[i] + msg[i + 1])
    print(alphabet[letter], end='')