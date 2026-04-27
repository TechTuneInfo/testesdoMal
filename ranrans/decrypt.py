import os
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "key.key"
TARGET_DIR = "test_files"

# Load encryption key from file
def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()

# Decrypt a single file
def decrypt_file(filepath, key):
    f = Fernet(key)

    with open(filepath, "rb") as file:
        data = file.read()

    try:
        decrypted_data = f.decrypt(data)
    except InvalidToken:
        print(f"[!] Skipping (invalid key or file): {filepath}")
        return

    with open(filepath, "wb") as file:
        file.write(decrypted_data)

    print(f"[+] Decrypted: {filepath}")

# Find target files
def find_files(directory):
    files = []

    for root, _, filenames in os.walk(directory):
        for name in filenames:
            path = os.path.join(root, name)

            if not name.endswith(".key") and not name.endswith(".py"):
                files.append(path)

    return files

# Main execution
def main():
    key = load_key()
    files = find_files(TARGET_DIR)

    for file in files:
        decrypt_file(file, key)

    print("[+] Files successfully restored!")

if __name__ == "__main__":
    main()
