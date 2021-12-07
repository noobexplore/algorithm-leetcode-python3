class Solution:
    def isValid(self, s: str) -> bool:
        '''消消乐'''
        if len(s)%2 != 0:
            return False
        brack_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        valid_stack = []
        valid_stack.append(s[0])
        for i in range(1, len(s)):
            if len(valid_stack) > 0:
                if valid_stack[-1] in brack_dict.keys():
                    if brack_dict[valid_stack[-1]] == s[i]:
                        valid_stack.pop()
                    else:
                        valid_stack.append(s[i])
                else:
                    valid_stack.append(s[i])
            else:
                valid_stack.append(s[i])
        if len(valid_stack) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    s = '[]{}'
    solution = Solution()
    res = solution.isValid(s)
    pass
