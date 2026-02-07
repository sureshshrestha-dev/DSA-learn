class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def print_linked_list(head):
    print(" -> ".join(map(str, linked_list_to_list(head))))
