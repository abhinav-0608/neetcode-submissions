class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        mySet = set()
        maxCount = 0


        for j in range(len(nums)):
            mySet.add(nums[j])


        for i in range(len(nums)):
            count = 1
            current = nums[i]
            if current - 1 not in mySet:
                while current + 1 in mySet:
                    current +=1
                    count += 1
                if count > maxCount:
                    maxCount = count
        
        return maxCount
        