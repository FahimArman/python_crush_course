import unittest

from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formated_name = get_formated_name('james', 'jack')
		self.assertEqual(formated_name, 'James Jack')

unittest.main()

