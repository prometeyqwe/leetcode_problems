"""
Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new length. Do not allocate extra space for
another array, you must do this by modifying the input array in-place with O(1)
extra memory
"""


class Solution:
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)


if __name__ == '__main__':
    s1 = Solution()
    print(s1.removeDuplicates([1, 1, 2]))
    print(s1.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
