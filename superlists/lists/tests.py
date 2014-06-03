from django.test import TestCase
import os
from django.conf import settings
#os.environ['DJANGO_SETTINGS_MODULE'] = 'superlists.settings'
settings.configure()

class SmokeTest(TestCase):
    
    def test_bad_math(self):
        self.assertEquals(1,2)
    
