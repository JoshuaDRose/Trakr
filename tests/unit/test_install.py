# Test all logic based interactions in test_install.py

import src.install
import unittest
import requests

class TestLoadDependencies(unittest.TestCase):

    def test_datatype(self):
        self.assertIsInstance(src.install(), dict)

    def test_network(self):
        response = requests.get('https://api.github.com/')
        self.assertEquals(response.status_code, 200)
