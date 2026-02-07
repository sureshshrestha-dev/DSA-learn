from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Initialize queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1
                
    if fresh_count == 0:
        return 0
        
    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue and fresh_count > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))
                    
    return minutes if fresh_count == 0 else -1

if __name__ == "__main__":
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    
    res = oranges_rotting(grid)
    print(f"Time to rot all oranges: {res} minutes")
    assert res == 4
    print("Rotten Oranges tests passed!")
