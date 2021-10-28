def reverse(x: int) -> int:
    s = list(str(x))
    i,j = 0, len(s)-1
    while(i<j):
        if s[i] == '-':
            i += 1
            continue
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1
    s = int("".join(s))
    if s>=-2**31 and s<=2**31:
        return s
    else:
        return 0


if __name__ == '__main__':
    s = 120
    print(reverse(s))
