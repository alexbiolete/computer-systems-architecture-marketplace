"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

import threading


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.producer_list = []
        self.cart_list = []
        self.producer_id = 0
        self.cart_id = 0

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.producer_list.append([])
        with threading.Lock():
            self.producer_id = len(self.producer_list) - 1
        return self.producer_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        reference = product[0]
        quantity = product[1]
        if len(self.producer_list[producer_id]) + quantity >= self.queue_size_per_producer:
            return False
        self.producer_list[producer_id].append(reference)
        with threading.Lock():
            quantity -= 1
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.cart_list.append([])
        with threading.Lock():
            self.cart_id = len(self.cart_list) - 1
        return self.cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for producer in self.producer_list:
            if product in producer:
                producer.remove(product)
                self.cart_list[cart_id].append(product)
                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        if product in self.cart_list[cart_id]:
            self.cart_list[cart_id].remove(product)
            self.producer_list[0].append(product)

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.cart_list[cart_id]
