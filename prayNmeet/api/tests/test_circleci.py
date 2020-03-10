from django.test import TestCase

# Create your tests here.

class TestCircleCi(TestCase):
    def test_circleci(self):
        self.assertEqual(2+2, 4)
