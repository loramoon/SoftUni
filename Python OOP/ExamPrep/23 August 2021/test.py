from unittest import TestCase, main

from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library1 = Library("Book")
        self.library2 = Library("Paper")
        self.library2.books_by_authors = {"A": ["B"]}
        self.library2.readers = {"C": ["D"]}

    def test_init_ok(self):
        self.assertEqual("Book", self.library1.name)
        self.assertEqual({}, self.library1.books_by_authors)
        self.assertEqual({}, self.library1.readers)

    def test_no_name_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.library1 = Library("")
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_if_author_not_in_list(self):
        self.library2.add_book("W", "O")
        self.assertEqual({'A': ['B'], 'W': ['O']}, self.library2.books_by_authors)

    def test_add_book_if_title_not_in_list(self):
        self.library2.add_book("W", "O")
        self.library2.add_book("W", "1")
        self.assertEqual({'A': ['B'], 'W': ['O', '1']}, self.library2.books_by_authors)

    def test_add_book(self):
        self.library2.add_book("A", "B")
        self.assertEqual({'A': ['B']}, self.library2.books_by_authors)

    def test_add_reader_if_name_not_in_list(self):
        self.library1.add_reader("K")
        self.assertEqual({"K": []}, self.library1.readers)

    def test_add_existing_reader(self):
        result = self.library2.add_reader("C")
        self.assertEqual("C is already registered in the Paper library.", result)

    def test_rent_book_if_reader_not_in_list(self):
        result = self.library1.rent_book("A", "B", "C")
        self.assertEqual("A is not registered in the Book Library.", result)

    def test_rent_book_if_author_not_in_list(self):
        result = self.library2.rent_book("C", "O", "I")
        self.assertEqual("Paper Library does not have any O's books.", result)

    def test_rent_book_if_title_not_in_list(self):
        result = self.library2.rent_book("C", "A", "I")
        self.assertEqual('Paper Library does not have A\'s \"I\".', result)

    def test_rent_book_all_ok(self):
        self.library2.rent_book("C", "A", "B")
        self.assertEqual({'C': ['D', {'A': 'B'}]}, self.library2.readers)
        self.assertEqual({'A': []}, self.library2.books_by_authors)


if __name__ == '__main__':
    main()
