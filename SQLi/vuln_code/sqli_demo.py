import sqlite3

# Step 1: Create a connection to a local database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Step 2: Create a users table (only if it doesn't exist)
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# Step 3: Insert a sample user (only for demo purposes)
cursor.execute("DELETE FROM users")  # Clear old data
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
conn.commit()

# Step 4: Ask for user input (this is where SQLi can happen)
username = input("Enter your username: ")

# Step 5: VULNERABLE QUERY - direct input into SQL statement
query = f"SELECT * FROM users WHERE username = '{username}'"
print("\n[DEBUG] Executing:", query)
cursor.execute(query)
result = cursor.fetchall()

# Step 6: Show result
if result:
    print("\n✅ User found:", result)
else:
    print("\n❌ No user found")

conn.close()


