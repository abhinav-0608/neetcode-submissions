class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        filledSet = set(nums)
        maxCount = 0
        
        # for j in range(len(nums)):
        #     filledSet.add(nums[j])
        
        for i in range(len(nums)):
            count = 1
            current = nums[i]
            if current - 1 not in filledSet:
                while current + 1 in filledSet:
                    count += 1
                    current += 1
            
            if count > maxCount:
                maxCount = count
        
        return maxCount




        