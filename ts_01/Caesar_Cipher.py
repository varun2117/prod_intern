def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))

    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
