import hashlib
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com":hash_password("password123"),
    "admin@example.com":hash_password("adminpass")

}

def login(email,password):
  if email in stored_logins:
    return stored_logins[email] == hash_password(password)
    return False

if __name__=="__main__":
  email =input("Emter yor email: ")
  password = input("Enter your password: ")


if login(email,password):
  print("Login successful!")
else:
  print("Invelid eamail or password.")
