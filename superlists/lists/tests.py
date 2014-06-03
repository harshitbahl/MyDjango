from django.test import TestCase
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'lists.settings'

class SmokeTest(TestCase):
    
    def test_bad_math(self):
        self.assertEquals(1,2)
    
