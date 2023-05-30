import unittest
from pyspark_test import assert_pyspark_df_equal

from index import createMyDataFrame 

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    
    def test_dataframe(self):
        assert_pyspark_df_equal(createMyDataFrame() , createMyDataFrame())

if __name__ == '__main__':
    unittest.main()
