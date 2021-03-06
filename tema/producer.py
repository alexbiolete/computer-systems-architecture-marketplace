"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        Thread.__init__(self, **kwargs)
        self.producer_id = 0

    def run(self):
        self.producer_id = self.marketplace.register_producer()
        while 1:
            for product in self.products:
                quantity = product[1]
                timeout = product[2]
                while 1:
                    if quantity == 0:
                        break
                    ret = self.marketplace.publish(self.producer_id, product)
                    if ret:
                        time.sleep(timeout)
                        quantity -= 1
                    else:
                        time.sleep(self.republish_wait_time)
