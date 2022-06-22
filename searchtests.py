from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r'E:\descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    """
    Con esta función lo que hace es escribir tee y buscar en la página ese producto
    el send_keys es el método que recibe el string y ya se le aplica el submit para que
    envíe y haga la búsqueda
    """
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
    """
    Con esta función lo que hace es escribir salt shaker y buscar en la página ese producto
    el send_keys es el método que recibe el string y ya se le aplica el submit para que
    envíe y haga la búsqueda
    """
    def test_search_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        #Con este línea lo que se hace es verificar que sea un producto
        self.assertEqual(1, len(products))
    
    #Con esta función se hace el cierre de la ventana cuando termina la búsqueda
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)