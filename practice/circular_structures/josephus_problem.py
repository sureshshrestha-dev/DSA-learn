class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def josephus_linked_list(n, k):
    if n == 1:
        return 1
    
    # Create circular linked list
    head = Node(1)
    curr = head
    for i in range(2, n + 1):
        curr.next = Node(i)
        curr = curr.next
    curr.next = head # Make it circular
    
    # Eliminate every k-th node
    while curr.next != curr:
        # Move k-1 steps
        for _ in range(k - 1):
            curr = curr.next
        # Delete next node
        # print(f"Eliminating: {curr.next.val}")
        curr.next = curr.next.next
        
    return curr.val

# Mathematical recursive approach for reference
def josephus_recursive(n, k):
    if n == 1:
        return 1
    return (josephus_recursive(n - 1, k) + k - 1) % n + 1

if __name__ == "__main__":
    n, k = 7, 3
    winner = josephus_linked_list(n, k)
    print(f"Winner (n={n}, k={k}): {winner}")
    assert winner == 4
    assert josephus_recursive(n, k) == 4
    print("Josephus tests passed!")
