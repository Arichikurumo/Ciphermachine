# ROT13 Implementation Script

def rot13Encrypt(text):
    result = []

    for char in text:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Rotate the character by 13 within the uppercase letters
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            # Rotate the character by 13 within the lowercase letters
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        
        else:
            # If it's not a letter, keep it unchanged
            result.append(char)
    
    return ''.join(result)

def rot13Decrypt(text):
    result = []

    for char in text:
        # Check if the character is an uppercase letter
        if 'A' <= char <= 'Z':
            # Rotate the character by 13 within the uppercase letters
            result.append(chr((ord(char) - ord('A') - 13) % 26 + ord('A')))
        
        # Check if the character is a lowercase letter
        elif 'a' <= char <= 'z':
            # Rotate the character by 13 within the lowercase letters
            result.append(chr((ord(char) - ord('a') - 13) % 26 + ord('a')))
        
        else:
            # If it's not a letter, keep it unchanged
            result.append(char)
    
    return ''.join(result)