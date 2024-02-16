from abc import ABC, abstractmethod
from entity.model.Customer import Customer
from entity.model.Product import Product

class ServiceProvider(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer):
        pass

    @abstractmethod
    def update_customer(self, customer: Customer):
        pass

    @abstractmethod
    def get_customer(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        pass

    @abstractmethod
    def get_products(self) -> list:
        pass

    # Define other methods as needed
