# Marks, Percentage and Placement Eligibility

m1 = float(input())
m2 = float(input())
m3 = float(input())

total = m1 + m2 + m3
percentage = (total / 300) * 100

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("pass")
else:
    print("fail")

print(total)
print(percentage)

if percentage >= 60:
    print("eligible for placement")
else:
    print("not eligible for placement")
    
