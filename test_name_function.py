import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py. """
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_nanme = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_nanme, 'Janis Joplin')
unittest.main()

