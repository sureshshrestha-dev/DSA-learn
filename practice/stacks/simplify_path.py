def simplify_path(path):
    stack = []
    parts = path.split("/")
    
    for p in parts:
        if p == "..":
            if stack:
                stack.pop()
        elif p == "." or not p:
            continue
        else:
            stack.append(p)
            
    return "/" + "/".join(stack)

if __name__ == "__main__":
    paths = [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c")
    ]
    
    for p, expected in paths:
        res = simplify_path(p)
        print(f"Path: {p} -> {res}")
        assert res == expected
    print("Simplify Path tests passed!")
