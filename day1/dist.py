from collections import Counter

f = open("input.txt", "r")

ls1 = []
ls2 = []

for x in f:
    ls = x.split("   ")
    a = ls[0]
    b = ls[1]
    bDigit = ""
    for i in b:
        if i.isdigit():
            bDigit += i
    ls1.append(int(a))
    ls2.append(int(b))

ls1.sort()
ls2.sort()

sum = 0
for i in range(len(ls1)):
    sum += abs(ls1[i] - ls2[i])

d = Counter(ls2)

score = 0
for i in ls1:
    score += d[i] * i

print(sum)
print(score)