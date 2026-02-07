def reverse_string(s):
    stack = list(s)
    res = ""
    while stack:
        res += stack.pop()
    return res

if __name__ == "__main__":
    test_str = "antigravity"
    reversed_str = reverse_string(test_str)
    print(f"Original: {test_str}, Reversed: {reversed_str}")
    assert reversed_str == test_str[::-1]
    print("Reverse String test passed!")
