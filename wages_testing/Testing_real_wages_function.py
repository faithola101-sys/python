import unittest
from real_wages_function import daily_wages

class TestRealWagesFunction(unittest.TestCase):
      def test_real_wages_positive(self):
        self.assertEqual(daily_wages(80), 45000)
      
      def test_real_wages_50_and_59_percentage(self):
          self.assertEqual(daily_wages(55), 55 * 200 + 5000)
      
      def test_real_wages_60_to_69_percentage(self):
          self.assertEqual(daily_wages(65), 65 * 250 + 5000)

      def test_real_wages_negative(self):
         with self.assertRaises(ValueError):
            daily_wages(-25)
      
      def test_real_wages_zero(self):
          self.assertEqual(daily_wages(0),0 * 160 + 5000)

      def test_real_wages_invalid(self):
          with self.assertRaises(ValueError):
             daily_wages(120)

      
if __name__ =='__main__':
     unittest.main()