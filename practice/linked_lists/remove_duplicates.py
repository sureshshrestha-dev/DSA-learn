from utils import create_linked_list, linked_list_to_list

def remove_duplicates_sorted(head):
    if not head:
        return None
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def remove_duplicates_unsorted(head):
    if not head:
        return None
    seen = {head.val}
    curr = head
    while curr and curr.next:
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            seen.add(curr.next.val)
            curr = curr.next
    return head

if __name__ == "__main__":
    # Test Sorted
    l1 = create_linked_list([1, 1, 2, 3, 3])
    remove_duplicates_sorted(l1)
    res1 = linked_list_to_list(l1)
    print(f"Sorted Removed: {res1}")
    assert res1 == [1, 2, 3]
    
    # Test Unsorted
    l2 = create_linked_list([3, 1, 2, 1, 3, 4])
    remove_duplicates_unsorted(l2)
    res2 = linked_list_to_list(l2)
    print(f"Unsorted Removed: {res2}")
    assert res2 == [3, 1, 2, 4]
    
    print("Tests passed!")
