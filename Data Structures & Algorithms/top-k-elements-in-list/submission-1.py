class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hashmap = {}
        frequency = [ [] for i in range(len(nums) + 1)]
        result = []
        count = 0

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1
        
        for nums, cnt in hashmap.items():
            frequency[cnt].append(nums)

        for j in range(len(frequency) - 1, 0, -1):
            for num in frequency[j]:
                result.append(num)
                if len(result) == k:
                    return result

        






        