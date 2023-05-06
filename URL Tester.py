import unittest
from test_package import URLMaker


class URLTester(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.url = URLMaker("www.google.com")

    def test_1(self):
        """test base url"""
        self.assertEqual(self.url.get_base_url(), "www.google.com")

    def test_2(self):
        """test add one query"""
        output = self.url.new_url().add_query({"test": "test"}).end_url()
        self.assertEqual(output, "www.google.com?test=test")

    def test_3(self):
        """test add three queries"""
        output = self.url.new_url().add_query({"test": "test", "test1": "test1", "test2": "test2"}).end_url()
        self.assertEqual(output, "www.google.com?test=test&test1=test1&test2=test2")

    def test_4(self):
        """test single path"""
        output = self.url.new_url().add_path("test").end_url()
        self.assertEqual(output, "www.google.com/test")

    def test_5(self):
        """test multiple paths"""
        output = self.url.new_url().add_path("test").add_path("test1").add_path("test2").end_url()
        self.assertEqual(output, "www.google.com/test/test1/test2")

    def test_6(self):
        """test one path and one query"""
        output = self.url.new_url().add_path("test").add_query({"some-test": "some-answer"}).end_url()
        self.assertEqual(output, "www.google.com/test?some-test=some-answer")

    def test_7(self):
        """test url encoding paths"""
        output = self.url.new_url().add_path("This is just a test").end_url()
        self.assertEqual(output, "www.google.com/This%20is%20just%20a%20test")

    def test_8(self):
        """test url encoding queries"""
        output = self.url.new_url().add_path("hello there").add_query({"Some test": "Some value"}).end_url()
        self.assertEqual(output, "www.google.com/hello%20there?Some+test=Some+value")
