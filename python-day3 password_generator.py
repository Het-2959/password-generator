import secrets
import string

print("🔐 Password Generator")

# take input (safe way)
while True:
    try:
        length = int(input("Enter password length: "))
        break
    except:
        print("❌ Enter a number only!")

# characters
characters = string.ascii_letters + string.digits 
# generate password
password = ""

for i in range(length):
    password += secrets.choice(characters)

print("✅ Your Password:", password)
