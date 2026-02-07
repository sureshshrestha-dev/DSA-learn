import re

def is_valid_html(html):
    # Regex to find tags: <tag> or </tag>
    # Note: This is a simplified checker and won't handle attributes or self-closing tags perfectly.
    tags = re.findall(r'<(/?[a-zA-Z1-6]+)>', html)
    stack = []
    
    for tag in tags:
        if tag.startswith('/'):
            # Closing tag
            tag_name = tag[1:]
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        else:
            # Opening tag
            stack.append(tag)
            
    return len(stack) == 0

if __name__ == "__main__":
    html1 = "<html><body><h1>Title</h1><p>Paragraph</p></body></html>"
    html2 = "<html><body><h1>Title</h2></body></html>" # Mismatched
    html3 = "<div><span></span>" # Unclosed
    
    print(f"HTML 1 valid? {is_valid_html(html1)}")
    print(f"HTML 2 valid? {is_valid_html(html2)}")
    print(f"HTML 3 valid? {is_valid_html(html3)}")
    
    assert is_valid_html(html1) == True
    assert is_valid_html(html2) == False
    assert is_valid_html(html3) == False
    print("HTML Tag Checker tests passed!")
