# Count Occurrences of Substring

str_ = "ababababab"
target = "ab"
count = 0
index = 0

while True:
    index = str_.find(target, index)
    if index == -1:
        break
    count += 1
    index += len(target)

print(count)