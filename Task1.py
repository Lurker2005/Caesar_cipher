def encry(stri, shi):
    encrypted_str = ""
    for char in stri:
        if char.isprintable():  
            new_char = chr(((ord(char) - 32 + shi) % 95) + 32)
            encrypted_str += new_char
        else:
            encrypted_str += char  
    return encrypted_str

def dec(stri, shi):
    decrypted_str = ""
    for char in stri:
        if char.isprintable():  
            new_char = chr(((ord(char) - 32 - shi) % 95) + 32)
            decrypted_str += new_char
        else:
            decrypted_str += char  
    return decrypted_str

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue

    if n == 1:
        stri = input("Enter the text to encrypt: ")
        shi = int(input("Enter the shift value: "))
        print("Encrypted text:", encry(stri, shi))
    elif n == 2:
        stri = input("Enter the text to decrypt: ")
        shi = int(input("Enter the shift value: "))
        print("Decrypted text:", dec(stri, shi))
    elif n == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
