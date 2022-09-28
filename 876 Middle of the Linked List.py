# idea: if the total length of the list is n, then the middle element has position (n//2 + 1). We just need to point to that element when we traverse the list exactly once.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 1 # total number of the list elements
        middleNumber = 1 # initialize what middle number is
        middle = head # initialize what middle node is
        end = head

        while end.next:
            end = end.next
            n = n + 1
            middleNumberNeo = n//2 + 1
            if(middleNumber!=middleNumberNeo):
                middleNumber = middleNumberNeo
                middle = middle.next

        return middle
            
#if __name__ == '__main__':
#    s = Solution()
#    s.middleNode(head)


# Method 2: more straightforward. We can convert the singly linked list to a python list first. it saves some space but is also slow.

class Solution2:    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pyList = []   
        middle = head 
        while head:
            pyList.append(head.val)
            head = head.next

        for i in range(len(pyList)//2):
            middle = middle.next

        return middle
            