import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """创建一个继承unittest.TestCase的类"""

    def test_formatted_name1(self):
        self.assertEqual(get_formatted_name("zhang", "san"), "Zhang San")

    def test_formatted_name2(self):
        self.assertEqual(get_formatted_name("zha2ng", "sa3n"), "Zha2Ng Sa3N")

    def test_formatted_name3(self):
        self.assertEqual(get_formatted_name("1zhang", "san"), "1Zhang San")

    def test_formatted_name4(self):
        self.assertEqual(get_formatted_name("Li", "san"), "Li San")

    def test_formatted_name5(self):
        self.assertEqual(get_formatted_name("Miss Gao", "san"), "Miss Gao San")


unittest.main()