from dao.ServiceProvider import ServiceProvider
from entity.model.Customer import Customer
from entity.model.Product import Product
import sqlite3

class Implementation(ServiceProvider):
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_customer(self, customer: Customer):
        query = "INSERT INTO customers (name, email, password) VALUES (?, ?, ?)"
        self.cursor.execute(query, (customer.name, customer.email, customer.password))
        self.connection.commit()

    def update_customer(self, customer: Customer):
        query = "UPDATE customers SET name=?, email=?, password=? WHERE customer_id=?"
        self.cursor.execute(query, (customer.name, customer.email, customer.password, customer.customer_id))
        self.connection.commit()

    def get_customer(self, customer_id: int) -> Customer:
        query = "SELECT * FROM customers WHERE customer_id=?"
        self.cursor.execute(query, (customer_id,))
        row = self.cursor.fetchone()
        if row:
            return Customer(row[0], row[1], row[2], row[3])
        else:
            return None

    def add_product(self, product: Product):
        query = "INSERT INTO products (name, price, description, stockQuantity) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (product.name, product.price, product.description, product.stock_quantity))
        self.connection.commit()

    def delete_product(self, product_id: int):
        query = "DELETE FROM products WHERE product_id=?"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

    def get_products(self) -> list:
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        products = []
        for row in rows:
            products.append(Product(row[0], row[1], row[2], row[3], row[4]))
        return products

    # Define other methods as needed
