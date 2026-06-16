# ArrayList Basic Operations

g1 = []

for i in range(1, 6):
    g1.append(i)

print("Output of begin and end:")
for i in range(len(g1)):
    print(g1[i], end=" ")
print()

print("\nOutput of reverse begin and reverse end:")
for i in range(len(g1) - 1, -1, -1):
    print(g1[i], end=" ")
print()

print("\n Size :", len(g1))
print(" Capacity : (Not directly accessible in Python either)")
print(" Max_Size :", float('inf'))

print("\n at \t: g1[4] =", g1[4])
print(" front() \t: g1.front() =", g1[0])
print(" back() \t: g1.back() =", g1[-1])

# ArrayList Insert and Remove Operations

list_ = []
list_.append(2)
list_.append(3)
list_.append(4)
list_.append(5)
list_.insert(0, 1)
print(list_)
list_.pop(2)
print(list_)

