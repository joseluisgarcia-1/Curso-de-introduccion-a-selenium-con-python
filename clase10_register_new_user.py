from faulthandler import is_enabled
import unittest
from selenium import webdriver
"""
Creación de un usuario dentro de la página
"""
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        #se le coloca el método click() para que simule un click y despliegue el menú
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        #le vamos a decir que encuentre un elemento por el texto que está en su enlace y ese texto es Log In
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        """para validar que ese botón este habilitado es con un assertion y es con assertTrue, is_displayed() para verificar que está disponible
        y is_enabled() para verificar que está habilitado, luego de verificarlos hacemos click en el botón
        create_account_button.click()       
        """
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        """
        Vamos a verificar si estamos en la parte de creación de cuenta, y eso lo podemos saber con el título que tiene la pestaña
        assertEqual -> porque vamos a comparar una igualdad de que si el sitio tiene como nombre: CreateNew Customer Account
        """
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        #Vamos a verificar que esos campos estén habilitados con un assertions y lo hacemos de la siguiente manera

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )
        
        # Vamos a enviar los datos a cada uno de los campos y usamos el método send_keys(value)
        first_name.send_keys('Test Jose')
        middle_name.send_keys('TestDev')
        last_name.send_keys('Test Dev')
        email_address.send_keys('Testdev@gmail.com')
        news_letter_subscription.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)