from http.server import executable
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    
    #Con esta función se identifica si el field(campo) está presente
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))
    #Con esta función se identifica si el field(campo) está presente
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
    
    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value= what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ =='__main__':
    unittest.main(verbosity=2)