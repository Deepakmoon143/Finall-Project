users_db = {}
food_menu = {
    1: {"Name": "Tandoori Chicken (4 pieces)", "Price": 240},
    2: {"Name": "Vegan Burger (1 Piece)", "Price": 320},
    3: {"Name": "Truffle Cake (500gm)", "Price": 900},
}
orders_history = []


def register_user():
    full_name = input("Enter Full Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")

    
    users_db[email] = {
        "Full Name": full_name,
        "Phone Number": phone_number,
        "Address": address,
        "Password": password,
    }
    print("Registration successful!")


def login_user():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    
    if email in users_db and users_db[email]["Password"] == password:
        print("Login successful!")
        return email
    else:
        print("Login failed. Please check your email and password.")
        return None


def display_food_menu():
    print("Food Menu:")
    for item_id, item_info in food_menu.items():
        print(f"{item_id}. {item_info['Name']} [INR {item_info['Price']}]")


def place_new_order(user_email):
    display_food_menu()
    selected_items = input("Enter the numbers of items you want to order (comma-separated): ").split(",")
    order = {
        "User Email": user_email,
        "Items": [],
        "Total Price": 0,
    }

    for item_id in selected_items:
        item_id = int(item_id)
        if item_id in food_menu:
            item_info = food_menu[item_id]
            order["Items"].append(item_info["Name"])
            order["Total Price"] += item_info["Price"]

    orders_history.append(order)
    print("Order placed successfully!")


def display_order_history(user_email):
    print(f"Order History for {users_db[user_email]['Full Name']}:")
    for order in orders_history:
        if order["User Email"] == user_email:
            print(f"Items: {', '.join(order['Items'])}")
            print(f"Total Price: INR {order['Total Price']}")
            print("-" * 20)


def update_user_profile(user_email):
    print("Update Profile:")
    full_name = input("Enter Full Name: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    users_db[user_email]["Full Name"] = full_name
    users_db[user_email]["Phone Number"] = phone_number
    users_db[user_email]["Address"] = address
    print("Profile updated successfully!")


while True:
    print("\nWelcome to the Restaurant Application")
    print("1. Register")
    print("2. Log in")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        user_email = login_user()
        if user_email:
            while True:
                print("\nUser Dashboard:")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Log out")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    place_new_order(user_email)
                elif user_choice == "2":
                    display_order_history(user_email)
                elif user_choice == "3":
                    update_user_profile(user_email)
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
