from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_fit_transform(self):
        input_data = ['red',
                      'square',
                      'black',
                      'red',
                      'large']
        actual = fit_transform(input_data)
        expected = [
            ('red', [0, 0, 0, 1]),
            ('square', [0, 0, 1, 0]),
            ('black', [0, 1, 0, 0]),
            ('red', [0, 0, 0, 1]),
            ('large', [1, 0, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_fit_transform_raises_exception_on_input_type(self):
        input_data = 12345
        with self.assertRaises(TypeError):
            fit_transform(input_data)

    def test_fit_transform_isinstance(self):
        input_data = ['red',
                      'square',
                      'black',
                      'red',
                      'large']
        actual = fit_transform(input_data)
        expected = list
        self.assertIsInstance(actual, expected)

    def test_fit_transform_input_string(self):
        input_data = 'red'
        actual = fit_transform(input_data)
        expected = [
            ('red', [1])
        ]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
