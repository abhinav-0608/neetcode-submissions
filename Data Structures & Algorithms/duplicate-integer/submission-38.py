class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlist=[]

        for num in nums:
            if num in newlist:
                return True
            else:
                newlist.append(num)
        return False

        