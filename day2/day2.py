f = open("input.txt", "r")

def isReportSafe(ls):

    increasing = ls[-1] > ls[0]

    for i in range(1, len(ls)):
        diff = ls[i] - ls[i - 1]
        if abs(diff) not in [1, 2, 3]:
            return False
        if diff < 0 and increasing:
            return False
        elif diff > 0 and not increasing:
            return False
    return True

def tolerableIsReportSafe(ls):
    if isReportSafe(ls):
        return True
    
    for i in range(len(ls)): # remove one element
        temp = ls[0:i] + ls[i + 1:]
        if isReportSafe(temp):
            return True
    return False

res1 = 0
res2 = 0

for level in f:
    ls_level = level.split(" ")
    for i in range(len(ls_level)):
        ls_level[i] = int(ls_level[i])
    if isReportSafe(ls_level):
        res1 += 1
    if tolerableIsReportSafe(ls_level):
        res2 += 1

print(res1, res2)