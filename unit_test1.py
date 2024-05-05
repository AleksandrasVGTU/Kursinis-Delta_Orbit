import unittest

from Delta_orbit import GameObject
# deltas due to rendering in integers, erros after e-7 dont matter
class TestVectorConversion(unittest.TestCase):


    def test_vector_to_coordinates(self):
        # Test for angle 0
        x, y = GameObject.vector_to_coordinates(10, 0)
        self.assertAlmostEqual(x, 0, delta=0.1), 
        self.assertAlmostEqual(y, 10, delta=0.1)

        # Test for angle 90 degrees
        x, y = GameObject.vector_to_coordinates(5, 90)
        self.assertAlmostEqual(x, 5, delta=0.1)
        self.assertAlmostEqual(y, 0, delta=0.1)

        # Test for angle 180 degrees
        x, y = GameObject.vector_to_coordinates(5, 180)
        self.assertAlmostEqual(x, 0, delta=0.1)
        self.assertAlmostEqual(y, -5, delta=0.1)

        # Test for angle 270 degrees
        x, y = GameObject.vector_to_coordinates(5, 270)
        self.assertAlmostEqual(x, -5, delta=0.1)
        self.assertAlmostEqual(y, 0, delta=0.1)

    def test_coordinates_to_vector(self):
        # Test for coordinates (3, 4)
        vector, angle = GameObject.coordinates_to_vector(3, 4)
        self.assertAlmostEqual(vector, 5)
        self.assertAlmostEqual(angle, 53.130102, delta=0.1)

        # Test for coordinates (0, 5)
        vector, angle = GameObject.coordinates_to_vector(0, 5)
        self.assertAlmostEqual(vector, 5)
        self.assertAlmostEqual(angle, 90, delta=0.1)

        # Test for coordinates (-3, -4)
        vector, angle = GameObject.coordinates_to_vector(-3, -4)
        self.assertAlmostEqual(vector, 5)
        self.assertAlmostEqual(angle, -53.13, delta=0.1)

if __name__ == '__main__':
    unittest.main()
