from utils import create_linked_list, linked_list_to_list

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # Get length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
        
    k %= length
    if k == 0:
        return head
    
    # Move to the node before the new head
    curr = head
    for _ in range(length - k - 1):
        curr = curr.next
        
    new_head = curr.next
    curr.next = None
    tail.next = head
    
    return new_head

if __name__ == "__main__":
    l1 = create_linked_list([1, 2, 3, 4, 5])
    k = 2
    rotated = rotate_right(l1, k)
    res = linked_list_to_list(rotated)
    print(f"Rotated by {k}: {res}")
    assert res == [4, 5, 1, 2, 3]
    print("Test passed!")
