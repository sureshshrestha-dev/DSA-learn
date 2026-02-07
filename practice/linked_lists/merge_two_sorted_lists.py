from utils import ListNode, create_linked_list, linked_list_to_list

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    curr = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        
    curr.next = l1 or l2
    return dummy.next

if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = merge_two_sorted_lists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Merged List: {result}")
    assert result == [1, 1, 2, 3, 4, 4]
    print("Test passed!")
