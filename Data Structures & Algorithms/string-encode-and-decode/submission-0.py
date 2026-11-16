class Solution:

    def encode(self, strs: List[str]) -> str:

        count = 0
        newStrs = ""
        
        for i in range(len(strs)):
            count = len(strs[i])
            newStrs += str(count) + "#" + strs[i]
        
        return newStrs


    def decode(self, s: str) -> List[str]:

        decodedStr = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            decodedStr.append(s[j + 1 : j + length + 1])

            i = j + length + 1

        return decodedStr
        


        

