def countAndSay(n: int) -> str:
    i = 2
    num_str = '1'
    result_dict = {1: '1'}
    while i <= n:
        count = 0
        tmp_str = ""
        tmp = num_str[0]
        for k in num_str:
            if k == tmp:
                count += 1
            else:
                tmp_str += str(count) + tmp
                count = 1
                tmp = k
        if count > 0:
            tmp_str += str(count) + tmp
        num_str = tmp_str
        result_dict[i] = num_str
        i += 1
    return result_dict[n]


def countAndSay_recursion(n: int) -> str:
    if n == 1:
        return '1'
    s = countAndSay_recursion(n-1)
    start,end = 0,0
    l = []
    while end < len(s):
        while end<len(s) and s[start] == s[end]:
            end +=1
        l.append(str(end - start))
        l.append(s[start])
        start = end
    return ''.join(map(str,l))


if __name__ == '__main__':
    print(countAndSay_recursion(6))
