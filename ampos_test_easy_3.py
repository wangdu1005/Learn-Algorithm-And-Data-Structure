'''
Interviewee: Wangdu Lin
Email: wangdu1005@gmail.com
Test Date Time: 2018/03/26 10:00:00 AM
Programming Lauange: Python 2.7.10
Time complexity: O(n)
Space complexity: O(n)
'''

# Definition of ListNode
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    '''
    Idea of solution:
    I think if in one-way linked list has a circular loop, 
    then the last node's next will point to the start of the circular loop.
    Therefore, I add visited node into set(), if there is any node match 
    the visited set, which means it is the start node, 
    becasue One-way linked list's node should only appear once in the loop,
    and the last node's next should point to None in Python.
    '''
    def findCircularLinkedList(self, node):
        if node is None:
            return None

        linkedSet = set()
        # while loop ---> Time: O(n)
        while node:
            # set() add ---> Space: O(n)
            linkedSet.add(node)
            # set() membership-checking ---> Time: On average, O(1)
            if node.next in linkedSet:
                return node.next
            else:
                node = node.next

        return None

    '''
    Good coding style should not create circular object in the program.
    Therefore, I add a method to destory the circular linked list.
    '''
    def freeLinkedList(self, head):
        if head is None:
            return None

        linkedSet = set()
        while head:
            linkedSet.add(head)
            nextNode = head.next
            
            # As long as the node is no longer referenced, 
            # it would be freed from Python's garbage collection mechanism.
            del head
            if nextNode in linkedSet:
                nextNode = None

            head = nextNode

        result = 'Successfully Released Linked List.'
        return result

if __name__ == "__main__":
    print('=== Test Start ===')
    quiz = Solution()
    a = ListNode('a')
    b = ListNode('b')
    c = ListNode('c')
    d = ListNode('d')
    e = ListNode('e')
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c # return c node to the result.

    result = quiz.findCircularLinkedList(a)
    if result is not None:
        print("Find Circular Linked List's Node Result: " + result.val)
    else:
        print("Find Circular Linked List's Node Result: None")

    freeResult = quiz.freeLinkedList(a)
    print(freeResult)
    print('=== Test Over  ===')