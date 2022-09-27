# 383. Ransom Note

# Idea: Identify character one by one from ransomNote and drop it from magazine. Using string manipulation is much faster than list.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazineUpdated = magazine

        for i in ransomNote:
            if(i in magazineUpdated):
                magazineUpdated = magazineUpdated.replace(i,'',1)
            else:
                return False

        return True

if __name__=='__main__':
    s = Solution()
    s.canConstruct("aa","aab")        
    
            
        
        