def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_palindrome_2(num):
    return num == int(str(num)[::-1])
