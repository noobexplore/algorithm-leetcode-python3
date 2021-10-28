def firstUniqChar(s: str) -> int:
    result_dict = {}
    for i in range(len(s)):
        if s[i] not in result_dict.keys():
            result_dict[s[i]] = 1
        else:
            result_dict[s[i]] += 1
    result_dict = sorted(result_dict.items(), key=lambda x:x[1], reverse=False)
    if result_dict[0][0] < 2:
        return s.find(result_dict[0][0])
    else:
        return -1


if __name__ == '__main__':
    s = "aabb"
    print(firstUniqChar(s))
