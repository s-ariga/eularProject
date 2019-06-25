import pyperclip

text = pyperclip.paste().splitlines()

total = 0
for line in text:
    print(int(line))
    total += int(line)

print("Anser = {0}".format(total))


