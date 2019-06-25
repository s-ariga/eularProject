answer = 2**1000

str_answer = str(answer)

total = 0
for i in str_answer:
    total += int(i)

print(total)

print(sum(int(i) for i in str(2**1000)))
