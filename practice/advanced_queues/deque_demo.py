from collections import deque

def deque_tutorial():
    print("--- Python collections.deque Tutorial ---")
    
    # 1. Initialization
    d = deque([1, 2, 3])
    print(f"Initial deque: {d}")
    
    # 2. Appending (Right and Left)
    d.append(4)      # O(1)
    d.appendleft(0)  # O(1)
    print(f"After append(4) and appendleft(0): {d}")
    
    # 3. Popping (Right and Left)
    val_right = d.pop()     # O(1)
    val_left = d.popleft()  # O(1)
    print(f"Popped right: {val_right}, left: {val_left}")
    print(f"Current deque: {d}")
    
    # 4. Rotation
    d.rotate(1) # Shift right by 1
    print(f"Rotated right by 1: {d}")
    d.rotate(-1) # Shift left by 1
    print(f"Rotated left by 1: {d}")
    
    # 5. Fixed length deque (Circular Buffer)
    circular = deque(maxlen=3)
    for i in range(5):
        circular.append(i)
        print(f"Added {i}, circular buffer is now: {list(circular)}")

if __name__ == "__main__":
    deque_tutorial()
