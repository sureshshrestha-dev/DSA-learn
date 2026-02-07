from collections import deque

def max_sliding_window(nums, k):
    q = deque() # Stores indices
    res = []
    
    for i, n in enumerate(nums):
        # Remove elements out of window
        while q and q[0] <= i - k:
            q.popleft()
            
        # Maintain monotonic property (descending)
        while q and nums[q[-1]] < n:
            q.pop()
            
        q.append(i)
        
        # Start adding to results once window is full
        if i >= k - 1:
            res.append(nums[q[0]])
            
    return res

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = max_sliding_window(nums, k)
    print(f"Nums: {nums}, k: {k}")
    print(f"Window Max: {result}")
    assert result == [3, 3, 5, 5, 6, 7]
    print("Sliding Window Maximum tests passed!")
