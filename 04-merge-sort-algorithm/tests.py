import unittest

from merge_sort_algorithm import merge_sort

class Test(unittest.TestCase):
    
    def test_sort_numbers(self):
        
        numbers = [20,30,23,1,3,4,89,29,5,2,9,10,15]
        
        numbers_ordered = [1, 2, 3, 4, 5, 9, 10, 15, 20, 23, 29, 30, 89]
        
        merge_sort(numbers)
        self.assertEqual(numbers, numbers_ordered)

    def test_sort_numbers_negative(self):
        
        numbers = [10, -1, -24, 15, 20, 16, -2, 5, 4]
        
        numbers_ordered = [-24, -2, -1, 4, 5, 10, 15, 16, 20]

        merge_sort(numbers)
        self.assertEqual(numbers, numbers_ordered)
        
    def test_order_numbers_greater_than_100(self):
        
        numbers = [100, -1000, -240, 150, 200, 350, 10000, -100, -500,  -12000, -5000, 999]
        
        numbers_ordered = [-12000, -5000, -1000, -500, -240, -100, 100, 150, 200, 350, 999, 10000]

        merge_sort(numbers)
        self.assertEqual(numbers, numbers_ordered)


if __name__ == '__main__':
    unittest.main()

