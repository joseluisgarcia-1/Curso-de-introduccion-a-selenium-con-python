from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner #ayuda a orquestar cada una de las pruebas que se ejecuten,junto con los reportes
from selenium import webdriver #para comunicarnos con el navegador

class HelloWorld(unittest.TestCase):

    """
    para hacer que esas pruebas corran en una sola ventana y no sé esté cerrando se le coloca el
    @classmethod, y se le cambio el parametro self por cls en el parámetro de la función
    """

    #@classmethod
    #def setUp(cls):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'E:\descargas\chromedriver.exe')
        #cls.driver = webdriver.Chrome(executable_path= r'E:\descargas\chromedriver.exe')
        driver = self.driver
        #driver = cls.driver
        driver.implicitly_wait(50)
    
    #funciones para visitar las páginas
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    def test_visit_marca(self):
        self.driver.get('https://www.marca.com')

    #@classmethod
    #def tearDown(cls):
    def tearDown(self):
        #cls.driver.quit()
        self.driver.quit()


if __name__ =='__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', 
        report_name='hello-world-report'))
