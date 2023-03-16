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
#-------------------------------------------------------------------------------------------------------------------------------
# Easy
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        nn = 0
        while(n>0):
            r = n%10
            nn = nn * 10 + r
            n = n//10
        if nn == x: return True
s = Solution()
pn = s.isPalindrome(121)
#-------------------------------------------------------------------------------------------------------------------------------
# Medium
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll = 0
        for i in range(len(s)):
            #print("org str", s[i], "at pos", i)
            #print("--------------------------->")
            snew = s[i:]
            #print("*** New string", snew, "starting from", i, "pos")
            l = ''
            for j in range(len(snew)):
                #print("Iterating through snew", snew[j])
                if snew[j] not in l:
                    l = l + snew[j]
                else: break
                if len(l) > ll: ll = len(l)
                #print("substring is", l, "and length is", ll)
        return ll

sn = Solution()
s = "aab"
res = sn.lengthOfLongestSubstring(s)
#-------------------------------------------------------------------------------------------------------------------------------