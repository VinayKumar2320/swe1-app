from django.test import SimpleTestCase


class BasicTests(SimpleTestCase):
    def test_basic_assertion(self):
        self.assertEqual(1 + 1, 2)
