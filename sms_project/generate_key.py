import hashlib
import sys

def generate_key(token):
    salt = "MAGXXIC_VOT_SECRET_SALT_2024"
    return hashlib.sha256((token + salt).encode()).hexdigest()[:16].upper()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_key.py <YOUR_SYSTEM_TOKEN>")
    else:
        token = sys.argv[1]
        print(f"Activation Key: {generate_key(token)}")
