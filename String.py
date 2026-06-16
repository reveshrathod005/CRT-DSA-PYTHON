#  String Palindrome, Login and Space Count

def is_palindrome(username):
    left = 0
    right = len(username) - 1
    while left <= right:
        if username[left] != username[right]:
            return False
        left += 1
        right -= 1
    return True


username = input()
password = input()

len1 = len(username)
len2 = len(password)

if len1 == len2:
    print("login sucessfully")
else:
    print("Invalid credentials")

count = 0
for i in range(len(username)):
    if username[i] == ' ':
        count += 1
print(count)

print(is_palindrome(username))