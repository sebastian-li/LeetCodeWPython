# 1672. Richest Customer Wealth

# Idea: using list comprehension to return a list of sums, and then output the max.
# comment: a very straightforward idea, somehow performed faster than 94.78% of Python3 online submissions and use memory less than 73.89% of Python3 online submissions. I'm surprised.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumsList = [sum(i) for i in accounts]
        return max(sumsList)
        
