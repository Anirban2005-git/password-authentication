import hashlib

users = {}
plain_passwords = {}  

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    print("\n📝 SIGNUP")

    username = input("👤 Enter username: ")

    if username in users:
        print("User already exists")
        return

    password = input("🔒Enter password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match")
        return

    users[username] = hash_password(password)
    plain_passwords[username] = password  

    print("Signup successful")

    choice = input("Do you want to see your username and password? (Y/N): ").lower()

    if choice == "y":
        print("\n--- Your Credentials ---")
        print("Username:", username)
        print("Password:", password)
        print("------------------------")

def login():
    print("\n🔑 LOGIN")
    username = input("👤Enter username: ")

    if username not in users:
        print("User not found")
        return

    attempts = 0
    while attempts < 3:
        password = input("🔒Enter password: ")

        if users[username] == hash_password(password):
            print("Login successful")
            return
        else:
            print("Invalid password")
            attempts += 1

    choice = input("Too many attempts. Want to see saved credentials? (Y/N): ").lower()

    if choice == "y":
        print("\n--- Stored Credentials ---")
        print("Username:", username)
        print("Password:", plain_passwords[username])
        print("--------------------------")

def show_menu():
    print("🔐 Authentication System")
    print("📝 1. Signup")
    print("🔑 2. Login")
    print("❌ 3. Exit")


while True:
    show_menu()
    option = input("Choose option: ")

    if option == "1":
        signup()
    elif option == "2":
        login()
    elif option == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option")
