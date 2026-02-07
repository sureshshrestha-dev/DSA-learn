from utils import create_linked_list

def is_palindrome(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]

# O(1) space implementation (optional but better)
def is_palindrome_optimized(head):
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse second half
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # Compare halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

if __name__ == "__main__":
    l1 = create_linked_list([1, 2, 2, 1])
    l2 = create_linked_list([1, 2, 3])
    
    print(f"Is {1,2,2,1} palindrome? {is_palindrome_optimized(l1)}")
    print(f"Is {1,2,3} palindrome? {is_palindrome_optimized(l2)}")
    
    assert is_palindrome_optimized(l1) == True
    assert is_palindrome_optimized(l2) == False
    print("Tests passed!")
