from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class FactoryTest(TestCase):
    def setUp(self) -> None:
        self.factory1 = PaintFactory("Name1", 150)
        self.factory2 = PaintFactory("Name2", 100)
        self.factory1.valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        self.factory2.ingredients = {"white": 5}

    def test_init(self):
        self.assertEqual("Name1", self.factory1.name)
        self.assertEqual(150, self.factory1.capacity)
        self.assertEqual({}, self.factory1.ingredients)

    # def test_add_ingredient_no_allowed_ingredient_raise(self):
    #     with self.assertRaises(TypeError) as te:
    #         self.factory1.add_ingredient("black", 20)
    #     self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(te.exception))

    def test_add_new_allowed_product(self):
        self.factory1.add_ingredient('yellow', 20)
        self.assertEqual({"yellow": 20}, self.factory1.ingredients)

    # def test_add_existing_product(self):
    #     self.factory2.add_ingredient("white", 20)
    #     self.assertEqual({"white": 25}, self.factory2.ingredients)

    def test_add_ingredient_no_space_ok_ingredient_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.factory1.add_ingredient("white", 200)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_remove_ingredient_no_such_raise(self):
        with self.assertRaises(KeyError) as ke:
            self.factory1.remove_ingredient("brown", 5)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_bigger_quantity_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.factory2.remove_ingredient("white", 100)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
    #
    # def test_remove_ingredient_ok(self):
    #     self.factory2.remove_ingredient("white", 4)
    #     self.assertEqual({"white": 1}, self.factory2.ingredients)

    def test_repr(self):
        result = f"Factory name: Name2 with capacity 100.\n" \
                 f"white: 5\n"
        self.assertEqual(result, self.factory2.__repr__())

    def test_products_property_if_returns_ingredients(self):
        self.assertEqual(self.factory2.products, self.factory2.ingredients)


if __name__ == "__main__":
    main()
