import unittest

class TestMeasureTime(unittest.TestCase):
    def test_measure_time(self):
        def dummy_function(delay):
            time.sleep(delay)
            return "Done"

        result, elapsed_time = measure_time(dummy_function, 1)
        self.assertEqual(result, "Done")
        self.assertAlmostEqual(elapsed_time, 1.0, delta=0.1)  

    def test_measure_time_with_args(self):
        def add(a, b):
            return a + b

        result, elapsed_time = measure_time(add, 3, 4)
        self.assertEqual(result, 7)
        self.assertLess(elapsed_time, 0.001)  

    def test_measure_time_with_kwargs(self):
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        result, elapsed_time = measure_time(greet, "World", greeting="Hi")
        self.assertEqual(result, "Hi, World!")
        self.assertLess(elapsed_time, 0.001)  

if __name__ == "__main__":
    unittest.main()