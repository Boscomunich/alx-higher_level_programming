
    def test_9_1(self):
        """Test for public method update with wrong types in kwargs."""

        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as x:
            r1.update(id='hi')
        self.assertEqual("id must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            r1.update(height=65, x=2, width="hi")
        self.assertEqual("width must be an integer", str(x.exception))

    def test_13_0(self):
        """Test for public method to_dictionary."""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(r1 == r2)

    def test_13_1(self):
        """Test for public method to_dictionary with wrong args."""

        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
