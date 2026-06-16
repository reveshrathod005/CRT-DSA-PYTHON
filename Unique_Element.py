# First Unique Element using HashMap

arr = [1, 2, 3, 2, 1, 4, 5]

map = {}
for num in arr:
    map[num] = map.get(num, 0) + 1

for num in arr:
    if map[num] == 1:
        print(num)
        break