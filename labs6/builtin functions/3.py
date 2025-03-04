def palindrome(s):
    return s == s[::-1]

s = input()
if(palindrome(s)):
    print("Text is palindrome")
else:
    print("Text is not palindrome")