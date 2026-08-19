class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        d = {}

        for i in range(len(strs)):
            signature = "".join(sorted(strs[i]))
            if signature not in d:
                d[signature] = []
            d[signature].append(strs[i])

        return list(d.values())
        
            

        