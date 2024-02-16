# from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
# from exception.CustomerNotFoundException import CustomerNotFoundException
# from exception.ProductNotFoundException import ProductNotFoundException
# from exception.OrderNotFoundException import OrderNotFoundException

# def main():
#     order_processor = OrderProcessorRepositoryImpl()

#     while True:
#         print("\n1. Register Customer")
#         print("2. Create Product")
#         print("3. Delete Product")
#         print("4. Add to Cart")
#         print("5. View Cart")
#         print("6. Place Order")
#         print("7. View Customer Order")
#         print("8. Exit")

#         choice = input("\nEnter your choice: ")

#         if choice == "1":
#             register_customer(order_processor)
#         elif choice == "2":
#             create_product(order_processor)
#         elif choice == "3":
#             delete_product(order_processor)
#         elif choice == "4":
#             add_to_cart(order_processor)
#         elif choice == "5":
#             view_cart(order_processor)
#         elif choice == "6":
#             place_order(order_processor)
#         elif choice == "7":
#             view_customer_order(order_processor)
#         elif choice == "8":
#             print("Exiting the application...")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# def register_customer(order_processor):
#     # Implement customer registration logic
#     pass

# def create_product(order_processor):
#     # Implement product creation logic
#     pass

# def delete_product(order_processor):
#     # Implement product deletion logic
#     pass

# def add_to_cart(order_processor):
#     # Implement add to cart logic
#     pass

# def view_cart(order_processor):
#     # Implement view cart logic
#     pass

# def place_order(order_processor):
#     # Implement place order logic
#     pass

# def view_customer_order(order_processor):
#     # Implement view customer order logic
#     pass

# if __name__ == "__main__":
#     main()

# ***************************************************************************************

from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException
from entity.model.Customer import Customer
from entity.model.Product import Product

class MainModule:
    def __init__(self):
        self.order_processor = OrderProcessorRepositoryImpl()

    def run(self):
        while True:
            print("\n1. Register Customer")
            print("2. Create Product")
            print("3. Delete Product")
            print("4. Add to Cart")
            print("5. View Cart")
            print("6. Place Order")
            print("7. View Customer Order")
            print("8. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.register_customer()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.delete_product()
            elif choice == "4":
                self.add_to_cart()
            elif choice == "5":
                self.view_cart()
            elif choice == "6":
                self.place_order()
            elif choice == "7":
                self.view_customer_order()
            elif choice == "8":
                print("Exiting the application...")
                break
            else:
                print("Invalid choice! Please try again.")

    def register_customer(self):
        print("Register Customer:")
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        password = input("Enter customer password: ")
        try:
            customer_id = self.order_processor.register_customer(Customer(name=name, email=email, password=password))
            print(f"Customer registered successfully with ID: {customer_id}")
        except CustomerNotFoundException:
            print("Error: Customer not found.")

    def create_product(self):
        print("Create Product:")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        description = input("Enter product description: ")
        stock_quantity = int(input("Enter product stock quantity: "))
        try:
            product_id = self.order_processor.create_product(Product(name=name, price=price, description=description, stock_quantity=stock_quantity))
            print(f"Product created successfully with ID: {product_id}")
        except ProductNotFoundException:
            print("Error: Product not found.")

    def delete_product(self):
        print("Delete Product:")
        product_id = int(input("Enter product ID to delete: "))
        try:
            self.order_processor.delete_product(product_id)
            print("Product deleted successfully.")
        except ProductNotFoundException:
            print("Error: Product not found.")

    def add_to_cart(self):
        print("Add to Cart:")
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        try:
            self.order_processor.add_to_cart(customer_id, product_id, quantity)
            print("Product added to cart successfully.")
        except (CustomerNotFoundException, ProductNotFoundException):
            print("Error: Customer or Product not found.")

    def view_cart(self):
        print("View Cart:")
        customer_id = int(input("Enter customer ID: "))
        try:
            cart = self.order_processor.view_cart(customer_id)
            print("Cart contents:")
            for item in cart:
                print(item)
        except CustomerNotFoundException:
            print("Error: Customer not found.")

    def place_order(self):
        print("Place Order:")
        customer_id = int(input("Enter customer ID: "))
        order_date = input("Enter order date (YYYY-MM-DD): ")
        total_price = float(input("Enter total price: "))
        shipping_address = input("Enter shipping address: ")
        try:
            order_id = self.order_processor.place_order(customer_id, order_date, total_price, shipping_address)
            print(f"Order placed successfully with ID: {order_id}")
        except CustomerNotFoundException:
            print("Error: Customer not found.")

    def view_customer_order(self):
        print("View Customer Order:")
        customer_id = int(input("Enter customer ID: "))
        try:
            orders = self.order_processor.view_customer_order(customer_id)
            print("Customer Orders:")
            for order in orders:
                print(order)
        except CustomerNotFoundException:
            print("Error: Customer not found.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()




