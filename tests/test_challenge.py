from unittest import TestCase
from challenge import ListChanger


class TestListChanger(TestCase):

	def setUp(self):
		self._list_changer_obj_1 = ListChanger([1, 2, 3, 4, 5, 6, 6])
		self._list_changer_obj_2 = ListChanger(["CA", "FL", "MC", "NY"])
		self._list_changer_obj_3 = ListChanger([True, False, True, False])
		
	def test_reverse_list(self):
		pass

	def test_has_duplicates(self):
		pass

	def test_smallest_number(self):
		pass

	def test_greatest_number(self):
		pass
	
	def test_second_greatest_number(self):
		pass
	
	def test_remove_first_and_last(self):
		pass

	def tearDown(self):
		self._list_changer_obj_1 = None
		self._list_changer_obj_2 = None
		self._list_changer_obj_3 = None
