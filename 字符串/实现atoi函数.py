import re
def myAtoi(s:str) -> int:
    # 第一步读入空格
    s = s.strip()
    if s == "":
        return 0
    i = 0
    int_list = []
    # 读入符号
    if s[0] == "-":
        int_list.append(s[0])
        i += 1
    if s[0] == "+":
        i += 1
    # 再读入剩余的数字
    for k in range(i, len(s)):
        if s[k].isdigit():
            int_list.append(s[k])
        else:
            break
    if len(int_list) == 1:
        if int_list[0] == "-":
            return 0
        else:
            s = "".join(int_list)
            s = int(s)
    elif len(int_list) > 1:
        s = "".join(int_list)
        s = int(s)
        if s < -2**31:
            s = -2**31
        elif s> 2**31 - 1:
            s = 2**31 - 1
    else:
        return 0
    return s



if __name__ == '__main__':
    s = "4193 with words"
    print(myAtoi(s))