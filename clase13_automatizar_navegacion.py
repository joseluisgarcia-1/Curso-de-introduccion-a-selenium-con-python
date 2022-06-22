import unittest
from selenium import webdriver
from time import sleep

"""
Script para realizar una búsqueda y automatizar las acciones del navegador
Como a veces ocurre muy rápido la ejecución del script lo que hacemos es controlar eso y lo hacemos con
importando unos submodulo y aplicandolos, aunque no se muy recomendable hacer esto en producción aquí lo hacemos a modo de ejemplo
no se recomienda porque lo tiempos de la prueba van a aumentar 
los submodulos importados son:

"""
class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('https://www.google.com/')


    def test_browser_navigation(self):
        driver = self.driver

        #identificaremos la barra de búsqueda la cual la va encontrar por su nombre
        search_field = driver.find_element_by_name('q')
        #con esto limpiamos una búsqueda previa que haya
        search_field.clear()
        #enviamos la búsqueda
        search_field.send_keys('platzi')
        search_field.submit()

        #Ahora vamos a avanzar, retroceder y refrescar una página
        #para retroceder
        driver.back()
        sleep(3)
        #para avanzar
        driver.forward()
        sleep(3)
        #para refrescar
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.implicitly_wait(50)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)