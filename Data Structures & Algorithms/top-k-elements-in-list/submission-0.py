class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for i in nums:
                hashmap[i] = hashmap.get(i , 0) + 1
        
        frequency = [ [] for i in range(len(nums) + 1)]
        
        for j in hashmap:
            frequency[hashmap[j]].append(j)
        
        result = []

        for x in range(len(frequency) - 1, 0, -1):
            for num in frequency[x]:
                result.append(num)
                if len(result) == k:
                    return result



            

            



        