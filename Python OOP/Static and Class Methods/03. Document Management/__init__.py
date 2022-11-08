from project.category import Category
from project.document import Document
from project.storage import Storage
from project.topic import Topic

import unittest


class TestDocumentManagement(unittest.TestCase):
    def setUp(self):
        self.c = Category(1, "C")
        self.t = Topic(1, "T", "C:\\user")
        self.d = Document(1, 1, 1, "D")
        self.s = Storage()

if __name__ == "__main__":
    unittest.main()