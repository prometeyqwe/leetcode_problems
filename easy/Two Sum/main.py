"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if target - nums[i] == nums[j] and i != j:
                    print([i, j])
                    return [i, j]

    def twoSum2(self, nums, target):
        nums_dict = {value: index for index, value in enumerate(nums)}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums_dict and nums_dict[temp] != i:
                print([i, nums_dict[temp]])
                return [i, nums_dict[temp]]

        print(nums_dict)

    def twoSum3(self, nums, target):
        d = dict()
        for i in range(len(nums)):
            n = target - nums[i]
            if n not in d:
                d[nums[i]] = i
            else:
                print([d[n], i])
                return [d[n], i]


if __name__ == '__main__':
    sol = Solution()
    sol.twoSum1(nums=[3, 2, 4], target=6)
    sol.twoSum2(nums=[3, 2, 4], target=6)
    sol.twoSum2(nums=[3, 2, 4], target=6)
