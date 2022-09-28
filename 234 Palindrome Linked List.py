#234. Palindrome Linked List

# Idea: convert singly linked list to a python list first and then use built in method to directly see if it's palindrome

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
    # traverse the whole list and save the result as a python list object    
        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next
   
    # use python's list function to see if it's palindrome    
        #return(nodeList==list(reversed(nodeList)))
        return(nodeList==nodeList[::-1]) # this is much faster
        
#if __name__ == '__main__':
#    s = Solution()
#    s.isPalindrome(head)        

