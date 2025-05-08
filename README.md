# 🛡️ Task 1: Caesar Cipher - Encryption & Decryption Tool

## 🔐 Description
This project is a simple Python-based Caesar Cipher tool that allows users to encrypt and decrypt messages. It uses a user-defined shift to rotate letters in the alphabet, preserving the original case and non-alphabet characters.

## 📌 Features
- Encrypt messages using a Caesar shift
- Decrypt messages with the same shift
- Keeps punctuation, spaces, and digits unchanged
- User-friendly command-line interface

## 🚀 How to Run

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)

2. **Run the Script**:
   Open a terminal or command prompt and execute:
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the Prompts**:
   - Type `E` to encrypt a message
   - Type `D` to decrypt a message
   - Enter your message and the shift value
   - Type `Q` to quit the program

## 🧠 How It Works
The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Example:
```
Original:  HELLO
Shift:     +3
Encrypted: KHOOR
```

For decryption, the shift is simply reversed.

## 💡 Sample Usage
```
Type 'E' to Encrypt or 'D' to Decrypt (Q to quit): E
Enter your message: Hello, World!
Enter shift value (number): 3
Encrypted Message: Khoor, Zruog!
```

## 👩‍💻 Author
Sneha K M
