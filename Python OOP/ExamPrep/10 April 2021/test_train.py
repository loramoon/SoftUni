from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train1 = Train("Train", 500)
        self.train2 = Train("Train2", 1)
        self.train2.passengers = ["A"]

    def test_init_ok(self):
        self.assertEqual("Train", self.train1.name)
        self.assertEqual(500, self.train1.capacity)
        self.assertEqual([], self.train1.passengers)

    def test_add_passenger_full_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.train2.add("C")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_same_passenger_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.train2.capacity = 2
            self.train2.add("A")
        self.assertEqual("Passenger A Exists", str(ve.exception))

    def test_add_new_passenger_ok(self):
        result = self.train1.add("A")
        self.assertEqual("Added passenger A", result)

    def test_remove_not_existing_passenger_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.train1.remove("A")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_ok(self):
        result = self.train2.remove("A")
        self.assertEqual("Removed A", result)



if __name__ == '__main__':
    main()