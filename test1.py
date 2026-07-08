import bcrypt

password = "MyPassword123"

salt = bcrypt.gensalt()

hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

print(f"Original password: {password}")
print(f"Hashed version: {hashed}")

entered_password = "MyPassword123"

is_valid = bcrypt.checkpw(entered_password.encode('utf-8'), hashed)

if is_valid:
    print("Login successful!")
else:
    print("Invalid password!")
