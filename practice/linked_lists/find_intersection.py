from utils import ListNode, create_linked_list

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    ptrA, ptrB = headA, headB
    
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
        
    return ptrA

if __name__ == "__main__":
    # Create intersection
    common = ListNode(8, ListNode(4, ListNode(5)))
    l1 = ListNode(4, ListNode(1, common))
    l2 = ListNode(5, ListNode(6, ListNode(1, common)))
    
    intersect = get_intersection_node(l1, l2)
    print(f"Intersection at node with value: {intersect.val if intersect else 'None'}")
    assert intersect == common
    print("Test passed!")
