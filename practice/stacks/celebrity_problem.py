def find_celebrity(matrix):
    n = len(matrix)
    stack = list(range(n))
    
    # Step 1: Find candidate
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if matrix[a][b]: # a knows b, a is not celebrity
            stack.append(b)
        else: # a doesn't know b, b is not celebrity
            stack.append(a)
            
    candidate = stack.pop()
    
    # Step 2: Verify candidate
    for i in range(n):
        if i != candidate:
            # Candidate must not know anyone AND everyone must know candidate
            if matrix[candidate][i] or not matrix[i][candidate]:
                return -1
    return candidate

if __name__ == "__main__":
    # matrix[i][j] means i knows j
    party = [[0, 1, 0],
             [0, 0, 0],
             [0, 1, 0]]
    
    celebrity = find_celebrity(party)
    print(f"Celebrity is person index: {celebrity}")
    assert celebrity == 1
    print("Celebrity Problem test passed!")
