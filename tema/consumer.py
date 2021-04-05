"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        Thread.__init__(self, **kwargs)
        self.cart_id = 0

    def run(self):
        for cart in self.carts:
            self.cart_id = self.marketplace.new_cart()
            for operation in cart:
                op_type = operation["type"]
                op_quantity = operation["quantity"]
                op_product = operation["product"]
                while 1:
                    if op_quantity == 0:
                        break
                    ret = False
                    if op_type == "add":
                        ret = self.marketplace.add_to_cart(self.cart_id, op_product)
                    elif op_type == "remove":
                        ret = self.marketplace.remove_from_cart(self.cart_id, op_product)
                    else:
                        continue
                    if ret is False:
                        time.sleep(self.retry_wait_time)
                    else:
                        op_quantity -= 1
            order = self.marketplace.place_order(self.cart_id)
            for product in order:
                print("%s bought %s" % (self.name, str(product)))
