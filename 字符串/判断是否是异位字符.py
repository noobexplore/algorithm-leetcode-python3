def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    all_dict = {}
    for sr in s:
        if sr not in all_dict.keys():
            all_dict[sr] = []
            all_dict[sr].append(1)
        else:
            all_dict[sr][0] += 1
    for tr in t:
        if tr not in all_dict.keys():
            return False
        else:
            if len(all_dict[tr]) == 1:
                all_dict[tr].append(1)
            else:
                all_dict[tr][1] += 1
    for k, v in all_dict.items():
        if all_dict[k][0] != all_dict[k][1]:
            return False
    return True

def isAnagram_v1(s: str, t: str) -> bool:
    s = sorted(s) 
    t = sorted(t)
    if s != t:
        return False
    else:
        return True
        


if __name__ == '__main__':
    s,t = "anagram", "nagarak"
    print(isAnagram_v1(s, t))