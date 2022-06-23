from cgitb import text
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DynaminControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver
        
        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()
        
        #esto hará que desaparezca el checkbox
        #le decimos que lo identifique por su selector de css
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')        
        remove_add_button.click()

        #para volver a hacer click en él
        """
        le decimos que espera 15 segundos como máximo hasta que la condición esperada (EC) sea clickable ->
        element_to_be_clickable y le indicamos cuál es el elemento y lo hacemos por su selector css
        By.CSS_SELECTOR, '#checkbox-example > button'
        """
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        #con esto aparece el checkbox nuevamente
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()

        #debemos haber esperado para que habilite el text area
        #crearemos una espera explícita con webdriverwait

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        #enable_disable_button.click()

        #le enviamos información y lo que le vamos a enviar es el texto platzi
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('platzi')
        #hacemos click para que lo deshabilite
        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()