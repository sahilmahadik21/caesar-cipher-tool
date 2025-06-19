def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def brute_force_decrypt(text):
    results = []
    for shift in range(1, 26):
        decoded = caesar_cipher(text, shift, mode='decrypt')
        results.append(f"Shift {shift}: {decoded}")
    return "\n".join(results)
