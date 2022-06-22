import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
"""
from selenium.webdriver.common.by import By esta nos ayuda a hacer referencia a un elemento delsitio web a través de sus selectores
no para identificarlo si no para interactuar distinto a como lo hace driver

from selenium.webdriver.support.ui import WebDriverWait este nos permite hacer uso de las expected conditions 

from selenium.webdriver.support import expected_conditions as EC este es para las 
"""

class ExplicitiWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\descargas\chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')

    #con esta función iremos al enlace que nos lleva a las cuentas del sitio
    def test_account_link(self):
        """
        en este diremos que webdrivewait hará referencia a self.driver y esperará máximo 10 segundos, hsta que se cumpla la condición esperada
        hacemos uso de una lambda que llamaremos s y con s diremos que nos encuentre el elemento con su id el cual será select-language
        que hace referencia al menú de selección de idiomas, y obtendremos su atributo con get_atribute, en este caso la longitud de los
        elementos que hay en este,es decir cuántos elementos hay en total, el cual lo igualaremos a 3 ya que sabemos que hay 3 opciones
        """
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')
        """hacemos un enlace donde están las cuentas webdrivewait hará referencia a self.driver y esperará máximo 10 segundos, hsta que se cumpla la condición esperada
            esa condición esperada la llamaremos EC y haciendo visibilidad al elemento que se está -> ubicando visibility_of_element_located
            para hacer referencia a este elemento lo vamos a hacer a través del texto que hay en el enlace y lo referenciamos con By.LINK_TEXT
            y el texto que hay en el que es ACCOUNT
        """
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        #aquí le decimos que haga click en account
        account.click()
    
    #con esta función nos llevará al enlace donde podemos crear un nuevo usuario
    def test_create_new_customer(self):
        """
        Le diremos que encuentre el elemento por el texto que hay en el enlace el cual será ACCOUNT y le haga click
        """
        self.driver.find_element_by_link_text('ACCOUNT').click()
        """creamos una variable donde webdrivewait hará referencia a self.driver y esperará máximo 10 segundos, hsta que se cumpla la condición esperada
            esa condición esperada la llamaremos EC y pueda identificar un elemento que esté visible -> ubicando visibility_of_element_located
            para hacer referencia a este elemento lo vamos a hacer a través del texto que hay en el enlace y lo referenciamos con By.LINK_TEXT
            y el texto que hay es My Account
        """
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))        
        my_account.click()        #Ahora a my_account le vamos a hacer un click
        sleep(30)
        
        """creamos una variable donde webdrivewait hará referencia a self.driver y esperará máximo 20 segundos, antes de que se cumpla la condición esperada
            esa condición esperada la llamaremos EC y es que un elemento pueda ser clickable -> element_to_be_clickable
            y lo identificaremos por el enlace del texto CREATE AN ACCOUNT
        """
        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click() #Ahora a create_account_button le vamos a hacer un click
        sleep(30)

        """
        ahora le vamos a decir a webdrivewait self.driver que el máximo de segundos que esperará que la condición se cumpla serán 10 que la condición esperada
        será EC.title_contains, es decir, va a verificar que el sitio web en su título contenga el siguiente texto
        Create New Customer Account
        """
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
        sleep(30)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)