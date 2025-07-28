# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # If the head is to be deleted
    if x == 1:
        return head.next

    # Initialize current node
    current = head
    count = 1

    # Traverse to the (x-1)-th node
    while current is not None and count < x - 1:
        current = current.next
        count += 1

    # Check if current and current.next exist before deletion
    if current is not None and current.next is not None:
        current.next = current.next.next

    return head
