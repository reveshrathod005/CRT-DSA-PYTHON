#  Recursion Functions and Unique Characters using Set

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def prime_number(n):
    if n == 0:
        return
    prime_number(n - 1)
    print(n)


def print_reverse(n):
    if n == 0:
        return
    print(n, end=" ")
    print_reverse(n - 1)


def reverse_string(s, index):
    if index < 0:
        return
    reverse_string(s, index - 1)
    print(s[index], end="")


def palindrome_string(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome_string(s, left + 1, right - 1)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


str_ = "aabbvvsjjdja"
union = set()
for ch in str_:
    union.add(ch)
print(union)

sb = ""
for ch in union:
    sb += ch
print(sb)