from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

sensitive = b"Credit card: 1234-5678-9012-3456"

encrypted = cipher.encrypt(sensitive)

print(f"Key: {key}")
print(f"Encrypted: {encrypted}")

decrypted = cipher.decrypt(encrypted)

print(f"Decrypted: {decrypted}")

wrong_key = Fernet.generate_key()
wrong_cipher = Fernet(wrong_key)
wrong_decrypted = wrong_cipher.decrypt(encrypted)
print(f"This should fail: {wrong_decrypted}")
