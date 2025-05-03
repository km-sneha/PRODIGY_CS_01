# Improved Caesar Cipher (User-Friendly)
# Still simple, not class-based
# By Sneha KM

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=" * 40)
    print("     Welcome to Caesar Cipher Tool     ")
    print("=" * 40)

    while True:
        choice = input("\nType 'E' to Encrypt or 'D' to Decrypt (Q to quit): ").upper()
        
        if choice == 'Q':
            print("Exiting... Thank you!")
            break

        if choice not in ['E', 'D']:
            print("Invalid choice. Please type E, D, or Q.")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value (number): "))
        except ValueError:
            print("Shift must be a number. Try again.")
            continue

        if choice == 'E':
            output = encrypt(message, shift)
            print("Encrypted Message:", output)
        else:
            output = decrypt(message, shift)
            print("Decrypted Message:", output)

# Run the program
main()
