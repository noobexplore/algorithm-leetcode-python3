class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        if s in roman_dict.keys():
            return roman_dict[s]
        i = 0
        num = 0
        while i < len(s):
            if s[i] not in ["I", "X", "C"]:
                num += roman_dict[s[i]]
                i += 1
            else:
                if s[i:i+2] in roman_dict.keys():
                    num += roman_dict[s[i:i+2]]
                    i += 2
                else:
                    num += roman_dict[s[i]]
                    i += 1
        return num


if __name__ == '__main__':
    s = "MCMXCIV"
    print(1^1)
    solution = Solution()
    n = solution.romanToInt(s)
    pass