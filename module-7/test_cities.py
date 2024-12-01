import unittest
from city_functions import city_country

class TestCityCountryFunction(unittest.TestCase):
    
    def test_city_country(self):
        # Test the city_country function with the given example
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile - population not found, language not found")
        
        result = city_country("New York", "United States", 5000000)
        self.assertEqual(result, "New York, United States - population 5000000, language not found")
        
        result = city_country("Tokyo", "Japan", 1600000, "Japanese")
        self.assertEqual(result, "Tokyo, Japan - population 1600000, Japanese")
# Run the test cases
unittest.main()