from unittest import TestCase

from total_avg import total_avg


class TestSumAverageFromFile(TestCase):

    def test_single_file(self):
        result = total_avg("foo4.txt")
        self.assertEquals(result, 8)

    def test_multiple_files(self):
        result = total_avg("foo1.txt")
        self.assertEquals(result, 4)
