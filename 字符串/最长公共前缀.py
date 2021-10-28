from typing import List


def longestCommonPrefix(strs:List[str]) -> str:
    min_len = 10000
    min_index = 0
    tmp_str = ''
    j = 0
    for i, item in enumerate(strs):
        if len(item) < min_len:
            min_index = i
            min_len = len(item)
    while j<min_len:
        for k in range(len(strs)):
            if strs[min_index][j] == strs[k][j]:
                tmp = strs[min_index][j]
            else:
                if j == 0:
                    return ""
                tmp = ""
                break
        if tmp == "":
            return tmp_str
        else:
            tmp_str += tmp
        j += 1
    return tmp_str


def longestCommonPrefix_zip(strs:List[str]) -> str:
    res = ''
    for ch in zip(*strs):
        if len(set(ch)) == 1:
            res += str(ch[0])
        else:
            break
    return res


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix_zip(strs))
            

