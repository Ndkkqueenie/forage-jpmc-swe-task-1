import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

    """ ------------ Add more unit tests ------------ """

    def test_getRatio(self):
        # Test case 1: Positive numbers
        price_a = 10
        price_b = 5
        assert getRatio(price_a, price_b) == 2.0

        # Test case 2: Zero values
        price_a = 0
        price_b = 100
        assert getRatio(price_a, price_b) == 0.0

        # Test case 3: Negative numbers
        price_a = -8
        price_b = 4
        assert getRatio(price_a, price_b) == -2.0

        # Test case 4: Decimal numbers
        price_a = 3.5
        price_b = 0.7
        assert getRatio(price_a, price_b) == 5.0

        # Test case 5: Large numbers
        price_a = 1000000
        price_b = 500000
        assert getRatio(price_a, price_b) == 2.0

        # Test case 6: price_b is zero (should raise ValueError)
        price_a = 10
        price_b = 0
        try:
            getRatio(price_a, price_b)
        except ValueError:
            pass  # Expected ValueError
        else:
            assert False, "Expected ValueError, but no exception was raised."

        print("All test cases passed!")


if __name__ == '__main__':
    unittest.main()
