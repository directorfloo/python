import string

def is_palindrome(text):
    
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

   
    stack = []

    
    for ch in cleaned:
        stack.append(ch)

   
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    
    return cleaned == reversed_text



print(is_palindrome("radar"))            # True
print(is_palindrome("Radar"))            # True (case-insensitive)
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("hello"))            # False
