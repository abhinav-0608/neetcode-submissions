class Solution:
    def isPalindrome(self, s: str) -> bool:

        emptyStr = ""
        newStr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                emptyStr = emptyStr + s[i]
        
        for j in range(len(emptyStr) - 1, -1, -1):
            newStr = newStr + emptyStr[j]
        
        if emptyStr.lower() == newStr.lower():
            return True
        return False

        