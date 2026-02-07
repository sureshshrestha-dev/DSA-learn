def largest_rectangle_area(heights):
    heights.append(0)
    stack = [-1]
    max_area = 0
    
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
        
    heights.pop() # Restore
    return max_area

if __name__ == "__main__":
    h = [2, 1, 5, 6, 2, 3]
    area = largest_rectangle_area(h)
    print(f"Heights: {h}, Max Area: {area}")
    assert area == 10
    print("Largest Rectangle in Histogram test passed!")
