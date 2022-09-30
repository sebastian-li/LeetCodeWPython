#1342. Number of Steps to Reduce a Number to Zero
# Idea: just to reduce the number to 0 and record how many steps were taken
# question: at the time of submission this is faster than 71.% submissions. Isn't this the most straightforward way to do it? How do others do it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
                
        n = 0
        
        while(num > 0):
            
            if( num % 2 == 0 ):
                num = num / 2
            else:
                num = num - 1
            n = n + 1

        return n
            

if __name__ == "__main__":
    s = Solution()
    s.numberOfSteps(14)            
    