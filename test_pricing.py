import unittest
from pricing import *


# The comments with each test explain how to calculate the pricing for
# each service Hiro offers. 
class TestPricing(unittest.TestCase):

    # Price is based on the square footage to be cleaned:
    # $200 for the first 500 square feet plus $100 for each additional
    # 250 square feet
    def test_clean_floor(self):
        self.assertEqual(clean_floor(501), 300)
        self.assertEqual(clean_floor(1500), 600)
        self.assertEqual(clean_floor(500), 200)
        self.assertEqual(clean_floor(0), -1)
        self.assertEqual(clean_floor(-125), -1)
        self.assertEqual(clean_floor(1), 200)
        self.assertEqual(clean_floor(490), 200)
        self.assertEqual(clean_floor(750), 300)
        self.assertEqual(clean_floor(800), 400)

    # Based on the roof material.
    # Inspecting a tile roof is $500; inspecting a shingle roof is $600.
    def test_inspect_roof(self):
        self.assertEqual(inspect_roof("tile"), 500)
        self.assertEqual(inspect_roof("SHINGLE"), 600)
        self.assertEqual(inspect_roof("tiLe"), 500)
        self.assertEqual(inspect_roof("shingle"), 600)
        self.assertEqual(inspect_roof("TILE"), 500)
        self.assertEqual(inspect_roof("shinGlE"), 600)
        self.assertEqual(inspect_roof("shingle  "), 600)
        self.assertEqual(inspect_roof("ti1e"), -1)
        self.assertEqual(inspect_roof("purple"), -1)
        self.assertEqual(inspect_roof(" tile"), 500)

    # Price is $100 per appliance, with an additional $500 if the customer
    # wants old appliances hauled away.
    def test_install_appliances(self):
        self.assertEqual(install_appliances(-20), -1)
        self.assertEqual(install_appliances(4, True), 900)
        self.assertEqual(install_appliances(2), 200)
        self.assertEqual(install_appliances(0), -1)
        self.assertEqual(install_appliances(2, False), 200)
        self.assertEqual(install_appliances(2, True), 700)
        self.assertEqual(install_appliances(3, False), 300)

    # Price combines the front yard cost and the back yard cost.
    # The front yard is $100 for up to 500 square feet and $150 for anything
    # larger than that.
    # The back yard is $125 for up to 400 square feet and $175 for a back
    # yard larger than 400 square fee.
    def test_yard_cleanup(self):
        self.assertEqual(yard_cleanup(400, 400), 225)
        self.assertEqual(yard_cleanup(0, 400), 225)
        self.assertEqual(yard_cleanup(400, 0), 225)
        self.assertEqual(yard_cleanup(500, 400), 225)
        self.assertEqual(yard_cleanup(501, 400), 275)
        self.assertEqual(yard_cleanup(600, 401), 325)
        self.assertEqual(yard_cleanup(1000, 1000), 325)

    # Based on the car widths of the garage. 1-car garage is $200;
    # 2-car garage is $300; 3-car garage = 375.
    # Invalid data should return -1
    def test_clean_garage(self):
        self.assertEqual(clean_garage(2), 300)
        self.assertEqual(clean_garage(1), 200)
        self.assertEqual(clean_garage(3), 375)
        self.assertEqual(clean_garage(4), -1)
        self.assertEqual(clean_garage(99), -1)
        self.assertEqual(clean_garage(-1), -1)
        self.assertEqual(clean_garage(0), -1)
        self.assertEqual(clean_garage("Two"), -1)

if __name__ == "__main__":
    unittest.main()