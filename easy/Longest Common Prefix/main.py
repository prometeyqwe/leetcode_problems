"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""
from typing import List
from functools import reduce
from itertools import zip_longest


class Solution:

    def LCP(self, a, b):
        res = []
        for i in zip_longest(a, b, fillvalue=''):
            if i[0] == i[1]:
                res.append(i[0])
            else:
                return ''.join(res)
        return ''.join(res)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = reduce(self.LCP, strs) if strs else ''
        return res if res else ''


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix([]))
    print(s.longestCommonPrefix(["", ""]))
    print(s.longestCommonPrefix(["c","c"]))
    print(s.longestCommonPrefix(["aca", "cba"]))
    print(s.LCP(*['qwe1', 'qwe2']))
