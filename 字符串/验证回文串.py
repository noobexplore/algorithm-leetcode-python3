def isPalindrome(s: str):
    n = len(s)
    i, j = 0, n-1
    while i<j:
        if not s[i].isalpha() and not s[i].isdigit():
            i += 1
            continue
        if not s[j].isalpha() and not s[j].isdigit():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    s = '0P'
    print(isPalindrome(s))