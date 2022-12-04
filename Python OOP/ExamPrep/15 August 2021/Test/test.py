from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Bau")
        self.shop2 = PetShop("Meow")
        self.shop2.food = {"vegan": 40}
        self.shop2.pets = ["Mote"]

    def test_init(self):
        self.assertEqual("Bau", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_zero_negative_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("banana", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_new(self):
        result = self.shop.add_food("mango", 5)
        self.assertTrue("mango" in self.shop.food)
        self.assertEqual({"mango": 5}, self.shop.food)
        self.assertEqual("Successfully added 5.00 grams of mango.", result)

    def test_add_food_exist(self):
        result = self.shop2.add_food("vegan", 5)
        self.assertTrue("vegan" in self.shop2.food)
        self.assertEqual({"vegan": 45}, self.shop2.food)
        self.assertEqual("Successfully added 5.00 grams of vegan.", result)

    def test_add_same_pet_raise(self):
        with self.assertRaises(Exception) as ex:
            self.shop2.add_pet("Mote")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_new_pet(self):
        result = self.shop2.add_pet("Kote")
        self.assertEqual("Successfully added Kote.", result)
        self.assertEqual(["Mote", "Kote"], self.shop2.pets)

    def test_feed_pet_no_name_raise(self):
        with self.assertRaises(Exception) as ex:
            self.shop2.feed_pet("tr", "Kote")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_no_food_name(self):
        result = self.shop2.feed_pet("meat", "Mote")
        self.assertEqual('You do not have meat', result)

    def test_feed_pet_add_food(self):
        result = self.shop2.feed_pet("vegan", "Mote")
        self.assertEqual(1040, self.shop2.food["vegan"])
        self.assertEqual("Adding food...", result)

    def test_fed_pet_decreasing_food(self):
        self.shop2.food = {"vegan": 140}
        result = self.shop2.feed_pet("vegan", 'Mote')
        self.assertEqual("Mote was successfully fed", result)
        self.assertEqual({"vegan": 40}, self.shop2.food)

    def test_repr_str(self):
        result = str(self.shop2)
        expected_result = f'Shop {self.shop2.name}:\n' \
                          f'Pets: {", ".join(self.shop2.pets)}'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
