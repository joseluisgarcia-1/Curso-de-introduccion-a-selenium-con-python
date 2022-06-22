import unittest
from selenium import webdriver

class CompareProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        #identificamos la barra de búsqueda que tiene como nombre q 
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        #enviaremos lo que queremos buscar con lo siguiente
        search_field.send_keys('tee')
        search_field.submit()

        #identificamos el elemento que vamos a agregar para comparar
        driver.find_element_by_class_name('link-compare').click()

        #ahora creamos el click para limpiar la lista de comparaciones
        driver.find_element_by_link_text('Clear All').click()
        self.driver.implicitly_wait(300)

        #le decimos al driver que haga un cambio de focus hacia el alerta
        alert = driver.switch_to.alert
        self.driver.implicitly_wait(300)
        alert_text = alert.text
        self.driver.implicitly_wait(300)

        #Ahora tenemos que verificar si el texto que muestra ese alert es el que queremos y hacemos la validación por medio de un assertEqual
        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
        self.driver.implicitly_wait(300)

        alert.accept()
        self.driver.implicitly_wait(300)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)