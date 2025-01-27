n = int(input())
record = 0
counter = 1
prev = 0
for i in input().split():
    i = int(i)
    if i == prev:
        counter += 1
    else:
        if (counter*prev)> record:
            record = (counter*prev)
        counter = 1
    prev = i

if (counter*prev)> record:
        record = (counter*prev)

print(str(record))