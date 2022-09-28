# 13. Roman to Integer

# Idea: interate numbers one by one. For each number, the default value of thisLoc is the number itself. 
# If it can be divided by 3, then change thisLoc to 'Fizz'
# If it can be devided by 5, and thisLoc hasn't been changed, then change thisLoc to 'Buzz'
# If it can be devided by 5, and thisLoc has been changed, then add 'Buzz' at the end of thisLoc  

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answerList = []

        for i in range(n):
            thisLoc = i_up = i + 1
            if(i_up % 3 == 0):
                thisLoc = 'Fizz'
            if(i_up % 5 == 0):
                if(isinstance(thisLoc, str)):
                    thisLoc = thisLoc + 'Buzz'
                else:
                    thisLoc = 'Buzz'
            answerList.append(str(thisLoc))

        return answerList


# Another idea: initialize the list as [1,2,...,n], then pick numbers that can be divided by 3 and change them to 'Fizz', do the same to numbers dividable by 5 and 15.
# Theoretically this should be faster. but since list has to be iterated multiple times, it's much slower than the last one!

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answerList = list(map(str, list(range(n+1))))
        answerList.pop(0)
        
        for i in ((np.array(range(n//3)) + 1 ) * 3):
            answerList[i-1] = 'Fizz'

        for i in ((np.array(range(n//5)) + 1 ) * 5):
            answerList[i-1] = 'Buzz'

        for i in ((np.array(range(n//15)) + 1 ) * 15):
            answerList[i-1] = 'FizzBuzz'
               
        return answerList


                            
            

if __name__ == '__main__':
    s = Solution()
    s.fizzBuzz(200)
                
            
            
            
            