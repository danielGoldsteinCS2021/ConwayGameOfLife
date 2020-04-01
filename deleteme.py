file = open("test.txt", 'r')
lines = file.readlines()
ls = []
for line in lines:
    line = line.strip()
    innerLs = []
    for value in line:
        innerLs.append(value)
    ls.append(innerLs)
ls = ls[1:]
print(ls)

'''
lines = file.readlines()
lengthOfLines = len(lines)
for i in range(lengthOfLines):
    cleaned = lines[i].strip()
'''
