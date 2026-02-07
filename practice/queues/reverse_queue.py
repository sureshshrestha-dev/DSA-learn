from collections import deque

def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    return q

if __name__ == "__main__":
    q = deque([1, 2, 3, 4, 5])
    print(f"Original Queue: {list(q)}")
    reverse_queue(q)
    print(f"Reversed Queue: {list(q)}")
    assert list(q) == [5, 4, 3, 2, 1]
    print("Reverse Queue test passed!")
