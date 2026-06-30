from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)

password = "Rohan@123"

hashed = hash_password(password)

print("Password:", password)
print("Hash:", hashed)

print("Verify:", verify_password(password, hashed))

token = create_access_token("1")

print("JWT:", token)

decoded = decode_access_token(token)

print(decoded)