# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        if not head:
            return [0]
        
        node = head
        
        # this stack will contain the elements that we don't know its next greater node
        # alongside its index, to insert in correct place
        stack = [(0, node.val)]
        node = node.next
        
        # starts the array with one element and increase it as we start iterating over the nodes
        result = [0] 
        i = 1
        while node:  # iterate over the linked list
            
            # do this until we find an element that is not greater that current node
            # or stack is empry
            while stack and node.val > stack[-1][-1]:
                    pos, val =  stack.pop()  # get index and value of top of stack
                    result[pos] = node.val  # update the greater element it the given index
            stack.append((i, node.val))
            node = node.next
            i += 1
            result.append(0)  # increase by 1 each new visited node
        
        # any element in the stack does not have a greater element
        while stack:
            pos, val = stack.pop()
            result[pos] = 0
        
        return result