import hashlib

def hash_password(password, salt):
    combined = salt + password
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    return hashed

password = "new_password"
salt = "new_salt"
hashed_password = hash_password(password, salt)
print(f"Hashed Password: {hashed_password}")