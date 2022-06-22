import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""
Este script lo que hace es cambiar el idioma de inglés a alemán y nuevamente a inglés
"""

#Para poder manipular un dropdown necesitamos importar el submodulo de selenium qué es: from selenium.webdriver.support.ui import Select
class SelectLanguage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        expo_options = ['English', 'French', 'German']
        act_options =[]
        #accederemos a las opciones y le indicaremos dónde está el dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))
        #vamos a validar que este dropdown tenga las 3 opciones de lenguaje, en donde indicamos la cantidad de opciones que hay
        # y lo comparamos con la longitud de la lista de opciones -> len(select_language.options
        self.assertEqual(3, len(select_language.options))

        #vamos a iterar por cada una de las opciones que tiene el dropdown y los agregamos a la lista vacía que es act_options
        #con append en dónde agregamos el texto de la opción más no la opción
        #act_options.append(option.text)
        for option in select_language.options:
            act_options.append(option.text)

        #verificamos que la lista de las opciones activas sean idénticas
        self.assertListEqual(expo_options, act_options)

        #seleccionamos un idioma de los que están disponibles para el ejemplo usamos English y con el first_selected_option validamos
        #que la primera palabra es English
        self.assertEqual('English', select_language.first_selected_option.text)

        #ahora le decimos que seleccione el idioma German
        select_language.select_by_visible_text('German')

        #Ahora verificamos que esté el idioma alemán
        self.assertTrue('store=german' in self.driver.current_url)

        #Ahora elegimos el idioma por medio del índice
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
