def check_palindrome(word: str) -> bool:
    s = ""
    for char in word:
        if char.isalnum():
            s += char.lower()

    left = 0
    right = len(s) - 1
    print(s)
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


print(check_palindrome("A man, a plan, a canal: Panama"))
print(check_palindrome("race a car"))
print(check_palindrome("1234321"))
