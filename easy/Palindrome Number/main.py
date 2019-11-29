"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        sint = str(x)
        return sint == sint[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
