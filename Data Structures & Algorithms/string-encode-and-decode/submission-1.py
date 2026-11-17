class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedStr = ""
        
        for i in range(len(strs)):
            count = len(strs[i])
            encodedStr += str(count) + "#" +strs[i]
        
        return encodedStr


    def decode(self, s: str) -> List[str]:

        i = 0
        decodedStr = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decodedStr.append(s[j + 1: j + length+ 1])
            i = j + length + 1
        return decodedStr
            
