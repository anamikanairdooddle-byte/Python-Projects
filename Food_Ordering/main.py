
import sqlite3

con = sqlite3.connect("food_ordering.db")
con.execute("PRAGMA foreign_keys = ON")
cur = con.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS food(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    price REAL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    food_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(food_id) REFERENCES food(id)
)
""")

# Create default admin
cur.execute(
    "INSERT OR IGNORE INTO users VALUES (1, 'admin', '1234', 'admin')"
)

# Add sample food
cur.execute("INSERT OR IGNORE INTO food VALUES (1, 'Burger', 120)")
cur.execute("INSERT OR IGNORE INTO food VALUES (2, 'Pizza', 250)")
cur.execute("INSERT OR IGNORE INTO food VALUES (3, 'Juice', 50)")
con.commit()


# Registration
def register():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "" or password == "":
        print("Input cannot be empty")
        return

    try:
        cur.execute(
            "INSERT INTO users(username, password, role) VALUES(?, ?, ?)",
            (username, password, "customer")
        )
        con.commit()
        print("Registration successful")

    except sqlite3.IntegrityError:
        print("Username already exists")


# Login
def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    cur.execute(
        "SELECT id, role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    if user is None:
        print("Invalid username or password")
        return

    user_id = user[0]
    role = user[1]

    if role == "admin":
        admin_menu()
    else:
        customer_menu(user_id)


# View food
def view_food():
    cur.execute("SELECT * FROM food")
    foods = cur.fetchall()

    print("\nID  Food       Price")
    for item in foods:
        print(item[0], item[1], item[2])


# Add food
def add_food():
    name = input("Food name: ").strip()

    if name == "":
        print("Name cannot be empty")
        return

    try:
        price = float(input("Price: "))

        if price <= 0:
            print("Price must be positive")
            return

        cur.execute(
            "INSERT INTO food(name, price) VALUES(?, ?)",
            (name, price)
        )
        con.commit()
        print("Food added")

    except ValueError:
        print("Enter a valid price")

    except sqlite3.IntegrityError:
        print("Food already exists")


# Update food
def update_food():
    view_food()

    try:
        food_id = int(input("Food ID to update: "))
        name = input("New food name: ").strip()
        price = float(input("New price: "))

        if name == "" or price <= 0:
            print("Invalid name or price")
            return

        cur.execute(
            "UPDATE food SET name=?, price=? WHERE id=?",
            (name, price, food_id)
        )

        if cur.rowcount == 0:
            print("Food ID not found")
        else:
            con.commit()
            print("Food updated")

    except ValueError:
        print("Enter valid values")

    except sqlite3.IntegrityError:
        print("Food name already exists")


# Delete food
def delete_food():
    view_food()

    try:
        food_id = int(input("Food ID to delete: "))

        cur.execute("DELETE FROM food WHERE id=?", (food_id,))

        if cur.rowcount == 0:
            print("Food ID not found")
        else:
            con.commit()
            print("Food deleted")

    except ValueError:
        print("Enter a valid ID")

    except sqlite3.IntegrityError:
        print("Cannot delete food used in an order")


# Place order
def place_order(user_id):
    view_food()

    try:
        food_id = int(input("Food ID: "))
        quantity = int(input("Quantity: "))

        if quantity <= 0:
            print("Quantity must be positive")
            return

        cur.execute("SELECT price FROM food WHERE id=?", (food_id,))
        food = cur.fetchone()

        if food is None:
            print("Food not found")
            return

        cur.execute(
            "INSERT INTO orders(user_id, food_id, quantity) VALUES(?, ?, ?)",
            (user_id, food_id, quantity)
        )
        con.commit()

        print("Order placed successfully")
        print("Total price:", food[0] * quantity)

    except ValueError:
        print("Enter valid numbers")


# View orders
def view_orders(user_id=None):
    if user_id is None:
        cur.execute("""
            SELECT orders.id, users.username, food.name,
                   orders.quantity, food.price * orders.quantity
            FROM orders
            JOIN users ON orders.user_id = users.id
            JOIN food ON orders.food_id = food.id
        """)
    else:
        cur.execute("""
            SELECT orders.id, food.name, orders.quantity,
                   food.price * orders.quantity
            FROM orders
            JOIN food ON orders.food_id = food.id
            WHERE orders.user_id=?
        """, (user_id,))

    orders = cur.fetchall()

    if not orders:
        print("No orders found")

    for order in orders:
        print(order)


# Admin menu
def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. View food")
        print("2. Add food")
        print("3. Update food")
        print("4. Delete food")
        print("5. View all orders")
        print("6. Logout")

        choice = input("Choice: ")

        if choice == "1":
            view_food()
        elif choice == "2":
            add_food()
        elif choice == "3":
            update_food()
        elif choice == "4":
            delete_food()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


# Customer menu
def customer_menu(user_id):
    while True:
        print("\n--- CUSTOMER MENU ---")
        print("1. View food")
        print("2. Place order")
        print("3. View my orders")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            view_food()
        elif choice == "2":
            place_order(user_id)
        elif choice == "3":
            view_orders(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice")


# Main menu
while True:
    print("\n--- ONLINE FOOD ORDERING SYSTEM ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    try:
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

    except sqlite3.Error as error:
        print("Database error:", error)

con.close()
print("Thank you!")
