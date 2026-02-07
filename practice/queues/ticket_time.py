from collections import deque

def time_required_to_buy(tickets, k):
    # k is the index of the person we are tracking
    queue = deque(enumerate(tickets))
    seconds = 0
    
    while queue:
        idx, count = queue.popleft()
        count -= 1
        seconds += 1
        
        if idx == k and count == 0:
            return seconds
            
        if count > 0:
            queue.append((idx, count))
            
    return seconds

# O(n) optimized version
def time_required_optimized(tickets, k):
    seconds = 0
    for i in range(len(tickets)):
        if i <= k:
            seconds += min(tickets[i], tickets[k])
        else:
            seconds += min(tickets[i], tickets[k] - 1)
    return seconds

if __name__ == "__main__":
    tix = [2, 3, 2]
    k_idx = 2
    res = time_required_to_buy(tix, k_idx)
    print(f"Tickets: {tix}, k={k_idx}, Time: {res}")
    assert res == 6
    assert time_required_optimized(tix, k_idx) == 6
    print("Time Needed to Buy Tickets tests passed!")
