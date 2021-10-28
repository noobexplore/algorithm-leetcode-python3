from typing import List


def strStr(haystack: str, needle: str):
    return haystack.find(needle)


def strStr_double_sub(haystack: str, needle: str):
    if needle == '':
        return 0
    n = len(haystack)
    m = len(needle)
    for i in range(n):
        if haystack[i:(i+m)] == needle:
            return i
    return -1


def get_next(next: List[int], patern: str) -> List:
    j = 0  # 指向前缀的末尾
    next[0] = 0  # 有的是-1有的是0开始
    for i in range(1, len(patern)):
        # 前缀与后缀不相等的情况
        while j > 0 and patern[i] != patern[j]:
            # j要开始回退到next[i-1]的索引位置
            j = next[j-1]
        # 前缀与后缀相等的情况
        if patern[i] == patern[j]:
            j += 1
            # 更新next数组
            next[i] = j
    return next


def KMP_strStr(haystack: str, needle: str):
    if needle == "":
        return 0
    i, j, next_list = 0, 0, [0]*len(needle)
    n = len(haystack)
    m = len(needle)
    next_list = get_next(next_list, needle)
    for i in range(n):
        while j>0 and haystack[i] != needle[j]:
            j = next_list[j-1]
        if haystack[i] == needle[j]:
            j += 1
        if j == m:
            return i - j + 1
    return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    print(KMP_strStr(haystack, needle))
