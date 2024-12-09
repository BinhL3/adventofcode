import re
# credits to reddit cause i dont know regex yet lol will come back to this again

with open('input.txt', 'r') as file:
    data = file.read()

pattern = r"mul\(\d+,\d+\)"
numbers = r"\d+,\d+"
muls = re.findall(pattern, data)

digits = [re.findall(numbers, i) for i in muls]

ls = []
for pair in digits:
    for subpair in pair:
        y = subpair.split(',')
        nums = [int(x) for x in y]
        ls.append(nums)

sum = 0
for num in ls:
    sum += num[0]*num[1]
print(sum)


pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
numbers = r"\d+,\d+"
muls = re.findall(pattern, data)

muls = ["x" if i == "don't()" else i for i in muls]
muls = ["y" if i == "do()" else i for i in muls]

digits = [re.findall(numbers,i) if i.__contains__("mul") else i for i in muls]

list_ = []
for pair in digits:
    for subpair in pair:
        nums = subpair.split(",")
        list_.append([int(i) if i != 'x' and i != 'y' else i for i in nums])

no_restriction = True
sum = 0

for i, pair in enumerate(list_):
    if pair[0] == 'x':
        no_restriction = False
    elif pair[0] not in ('x', 'y') and no_restriction:
        #print(i,pair)
        sum += pair[0]*pair[1]
    elif pair[0] == 'y':
        no_restriction = True
    
print(sum)

