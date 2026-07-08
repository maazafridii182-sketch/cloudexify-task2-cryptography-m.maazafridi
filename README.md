# Cryptography & Password Security Project

## CloudExify Cybersecurity Internship - Month 1, Project 2

## Kya Banaya Gaya Hai

Is project mein maine ye implement kiya hai:

1. **Password Hashing (bcrypt)** - Passwords ko secure tareeke se hash kiya jata hai, plaintext mein store nahi hota
2. **Symmetric Encryption (Fernet)** - Sensitive data ko encrypt/decrypt karna
3. **Secure Authentication System** - Complete user registration aur login system

## Files

- `secure_auth.py` - User registration aur login system (bcrypt hashing ke sath)
- `encryption_examples.py` - Fernet encryption/decryption examples
- `test1.py` - Basic bcrypt hashing examples

## Kaise Chalayein

python3 secure_auth.py
python3 encryption_examples.py

## Testing Kiya Gaya

- Bcrypt se hash generate karna
- Sahi password verify karna (Login successful)
- Galat password reject karna (Invalid password)
- Data encrypt/decrypt karna
- Galat encryption key se error (InvalidToken)
- Duplicate user registration reject karna (User exists)

## Security Best Practices Follow Ki Gayin

- Passwords kabhi bhi plaintext mein store nahi kiye
- Har password ka apna unique salt hai
- bcrypt use kiya (slow hashing, brute force se protection)
- Sensitive data encrypt kiya gaya hai
