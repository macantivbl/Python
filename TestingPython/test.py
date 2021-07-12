import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.suma(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'fdsafdsafdas'
        result = main.suma(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = main.suma(test_param)
        self.assertEqual(result, 'pon un numero')


unittest.main()
