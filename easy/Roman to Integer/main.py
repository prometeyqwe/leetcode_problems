"""
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4
"""


class Solution:
    d1 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        flag = False
        for i in range(len(s)):
            temp = s[i:i+2]
            if flag:
                flag = False
                continue
            if len(temp) > 1 and self.d1[temp[0]] < self.d1[temp[1]]:
                res += self.d1[temp[1]] - self.d1[temp[0]]
                flag = True
            else:
                res += self.d1[temp[0]]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('IX'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
