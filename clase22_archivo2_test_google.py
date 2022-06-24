from time import sleep
import unittest
from selenium import webdriver
from clase22_archivo1_google_page import GooglePage

class GoogleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')
        sleep(10)

        self.assertEqual('Platzi', google.keyword)
        sleep(10)

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)