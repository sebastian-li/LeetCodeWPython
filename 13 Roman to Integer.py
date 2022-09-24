# 13. Roman to Integer

# Idea: iterate from the leftmost character to the second to rightmost character. If it is smaller than its right neighbor, detract its corresponding value; otherwise, add it. Then add the value for the right most character.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        sumValue=0
        symbolDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for k in range(len(s)-1):
            if(symbolDict[s[k]]<symbolDict[s[k+1]]):
                sumValue=sumValue-symbolDict[s[k]]
            else:
                sumValue=sumValue+symbolDict[s[k]]
        sumValue= sumValue+symbolDict[s[len(s)-1]]        
        return sumValue
        
if __name__ == '__main__':
    s = Solution()
    s.romanToInt("III")        

