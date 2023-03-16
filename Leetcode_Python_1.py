# Easy
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (nums[i] + nums[j] == target):
                    l.append(i)
                    l.append(j)
        newList = list(set(l))
        return newList
num = [3,2,4]
target = 6
s = Solution()
list1 = s.twoSum(num,target)