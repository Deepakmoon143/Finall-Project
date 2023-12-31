import json

admins = []

class admin:
    def __init__(self, full_name, phone_number, email, address, password):
        self.admin_id = len(admins) + 1  
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

def register_admin():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Create a password: ")

    new_admin = admin(full_name, phone_number, email, address, password)
    admins.append(new_admin)
    print("\nRegistration successful!")

    with open('admins.json', 'a') as file:
        admin_data = {
            'admin_id': new_admin.admin_id,
            'full_name': new_admin.full_name,
            'phone_number': new_admin.phone_number,
            'email': new_admin.email,
            'address': new_admin.address,
            'password': new_admin.password
        }
        json.dump(admin_data, file)
        file.write('\n')



def login_admin():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for admin in admins:
        if admin.email == email and admin.password == password:
            return admin
    return None

def display_admin_details(admin):
    if admin:
        print("\nAdmin Details:")
        print(f"Admin ID: {admin.admin_id}")
        print(f"Full Name: {admin.full_name}")
        print(f"Phone Number: {admin.phone_number}")
        print(f"Email: {admin.email}")
        print(f"Address: {admin.address}")
        print(f"password: {admin.password}")
    else:
        print("\nNo admin logged in.")



if __name__ == '__main__':


    current_admin = None

    while True:
        print("\nAdmin Login/Register:")
        print("1. Register")
        print("2. Log in")
        print("3. Update Profile")
        print("4. Admin Details")
        print("5. Admin Menu")
        admin_choice = input("\nEnter your choice: ")

        if admin_choice == '1':
            register_admin()
        elif admin_choice == '2':
            current_admin = login_admin()
            if current_admin:
                print("\nLogin successful!")
            else:
                print("\nLogin failed. Please check your credentials.")
        elif admin_choice == '3':
            if current_admin:
                
                print("\nUpdate Profile:")

                full_name = input(f"Full Name ({current_admin.full_name}): ")
                phone_number = input(f"Phone Number ({current_admin.phone_number}): ") 
                address = input(f"Address ({current_admin.address}): ")
                
                
                current_admin.full_name = full_name
                current_admin.phone_number = phone_number
                current_admin.address = address
                
                print("\nProfile updated successfully!")
            
            else:
                print("\nPlease log in first.")

        elif admin_choice == '4':
            display_admin_details(current_admin)
           
        elif admin_choice =="5":
             
            if current_admin:
                break
            else:
                print("\nPlease log in first.")

        else:
            print("\nInvalid choice. Please try again.")

food_items = []


class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = len(food_items) + 1  
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

def add_food():
    name = input("Enter the food name: ")
    quantity = input("Enter the quantity (e.g., 100ml, 250gm, 4 pieces): ")
    price = float(input("Enter the price: "))
    discount = float(input("Enter the discount: "))
    stock = int(input("Enter the stock amount: "))

    new_food = FoodItem(name, quantity, price, discount, stock)
    food_items.append(new_food)
    print("\nFood item added successfully")


def edit_food(food_id):
    for food in food_items:
        if food.food_id == food_id:
            print(f"Editing FoodID {food_id}")
            food.name = input("Enter the new food name: ")
            food.quantity = input("Enter the new quantity: ")
            food.price = float(input("Enter the new price: "))
            food.discount = float(input("Enter the new discount: "))
            food.stock = int(input("Enter the new stock amount: "))
            print("Food item updated successfully")
            return
    print("\nFood item not found")



def view_food():
    print("\nList of Food Items:")
    for food in food_items:
        print(f"FoodID: {food.food_id}")
        print(f"Name: {food.name}")
        print(f"Quantity: {food.quantity}")
        print(f"Price: INR {food.price}")
        print(f"Discount: INR {food.discount}")
        print(f"Stock: {food.stock}")
        print("-----------------------")

def remove_food(food_id):
    for food in food_items:
        if food.food_id == food_id:
            food_items.remove(food)
            print("\nFood item removed successfully")
            return
    print("\nFood item not found")

if __name__ == '__main__':
    
    while True:
        print("\nAdmin Menu:")
        print("1. Add new food item")
        print("2. View all food items")
        print("3. Edit food item")
        print("4. Remove food item")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_food()
        elif choice == '2':
            view_food()    
        elif choice == '3':
            food_id = int(input("\nEnter FoodID to edit: "))
            edit_food(food_id)   
        elif choice == '4':
            food_id = int(input("\nEnter FoodID to remove: "))
            remove_food(food_id)
        elif choice == '5':
            break
        else:
            print("\nInvalid choice. Please try again.")



users = []
orders = []

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.user_id = len(users) + 1  
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class Order:
    def __init__(self, user_id, food_items):
        self.order_id = len(orders) + 1  
        self.user_id = user_id
        self.food_items = food_items


def register_user():
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Create a password: ")

    new_user = User(full_name, phone_number, email, address, password)
    users.append(new_user)
    print("\nRegistration successful!")


def login_user():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user in users:
        if user.email == email and user.password == password:
            return user
    return None


def place_order(user):
    print("\nAvailable food items:")
    food_items = [
        "Tandoori Chicken (4 pieces) [INR 240]",
        "Vegan Burger (1 Piece) [INR 320]",
        "Truffle Cake (500gm) [INR 900]"
    ]

    for i, item in enumerate(food_items, start=1):
        print(f"{i}. {item}")

    selected_items = input("Enter the numbers of the items you want to order (e.g., 2 3): ").split()
    selected_items = [int(item) for item in selected_items]

    order_details = [food_items[i - 1] for i in selected_items]

    order = Order(user.user_id, order_details)
    orders.append(order)
    print("\nOrder placed successfully!")


def order_history(user):
    user_orders = [order for order in orders if order.user_id == user.user_id]

    if user_orders:
        print("\nOrder History:")
        for order in user_orders:
            print(f"Order ID: {order.order_id}, Items: {', '.join(order.food_items)}")
    else:
        print("\nNo order history found for this user.")


def update_profile(user):
    print("\nUpdate Profile:")
    full_name = input(f"Full Name ({user.full_name}): ")
    phone_number = input(f"Phone Number ({user.phone_number}): ")
    email = input(f"Email ({user.email}): ")
    address = input(f"Address ({user.address}): ")
    password = input(f"Password ({user.password}): ")

    user.full_name = full_name
    user.phone_number = phone_number
    user.email = email
    user.address = address
    user.password = password

    print("\nProfile updated successfully!")

if __name__ == '__main__':
    
    user = None
    while True:
        print("\nUser Menu:")
        print("1. Register")
        print("2. Log in")
        print("3. Place New Order")
        print("4. Order History")
        print("5. Update Profile")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                print("\nLogin successful!")
            else:
                print("\nLogin failed. Please check your credentials.")
        elif choice == '3':
            if user:
                place_order(user)
            else:
                print("\nPlease log in first.")
        elif choice == '4':
            if user:
                order_history(user)
            else:
                print("\nPlease log in first.")
        elif choice == '5':
            if user:
                update_profile(user)
            else:
                print("\nPlease log in first.")
        elif choice == '6':
            break
        else:
            print("\nInvalid choice. Please try again.")
