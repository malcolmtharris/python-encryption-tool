from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())


def decrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.decrypt(message).decode()


def main():
    print(r"""
  _____                    _     _____                             _   _               _____           _ 
 |  ___|__ _ __ _ __   ___| |_  | ____|_ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __   |_   _|__   ___ | |
 | |_ / _ \ '__| '_ \ / _ \ __| |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \    | |/ _ \ / _ \| |
 |  _|  __/ |  | | | |  __/ |_  | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | |   | | (_) | (_) | |
 |_|  \___|_|  |_| |_|\___|\__| |_____|_| |_|\___|_|   \__, | .__/ \__|_|\___/|_| |_|   |_|\___/ \___/|_|
                                                       |___/|_|                                          
""")

    while True:
        print("\n1. Generate a new key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            key = generate_key()
            print("Your new key (save this!):", key.decode())

        elif choice == "2":
            text = input("Enter text to encrypt: ")
            key = input("Paste your key: ").encode()

            encrypted = encrypt_message(text, key)
            print("Encrypted:", encrypted.decode())

        elif choice == "3":
            token = input("Paste the encrypted text: ").encode()
            key = input("Paste your key: ").encode()

            try:
                decrypted = decrypt_message(token, key)
                print("Decrypted:", decrypted)
            except Exception:
                print("Decryption failed - wrong key or corrupted text.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
