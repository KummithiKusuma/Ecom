class Order:
    def __init__(self, order_id, customer_id, order_date, total_price, shipping_address):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__order_date = order_date
        self.__total_price = total_price
        self.__shipping_address = shipping_address

    # Getter and setter methods
