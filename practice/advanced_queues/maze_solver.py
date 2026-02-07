from collections import deque

def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == end:
            return path
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and \
               maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
                
    return None

if __name__ == "__main__":
    # 0 = open, 1 = wall
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    
    path = solve_maze(maze, start, end)
    print(f"Shortest path from {start} to {end}:")
    if path:
        for r, c in path:
            print(f"({r}, {c})", end=" -> ")
        print("Finish")
    else:
        print("No path found.")
        
    assert path is not None
    print("Maze Solver test passed!")
