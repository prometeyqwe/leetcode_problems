"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n = len(s)
        res = 0
        res_s = set()
        while i < n and j < n:
            if not s[j] in res_s:
                res_s.add(s[j])
                j += 1
                res = max(res, abs(i - j))
            else:
                res_s.remove(s[i])
                i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))

