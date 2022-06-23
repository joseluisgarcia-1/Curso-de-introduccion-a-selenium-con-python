import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_element(self):
        
        driver = self.driver

        options = []
        #número de opciones que habrá
        menu = 5
        #contará cuantos intentos le tomará a selenium lo inicamos en 1 porque al iniciar lo tomará como un intento
        tries = 1

        # mientras que la longitud de options sea menor que 5,se va estár repitiendo el código a continuación
        while len(options) < 5:
            #limpiar los valores que hay en options en cada ciclo
            options.clear()

            #vamos a iterar a través de las opciones
            for i in range(menu):
                #usamos el try except ya que puede que lleguemos al número 5 al valor del menú pero no se encuentre presente, así que es mejor evitarlo
                try:
                    #con esta variable vamos a guardar el elemento que se muestra en pantalla,que en este caso sería el botón
                    #tener en cueta qye le cambiamos que no tome la posición del botón si no que itere con lo siguiente [{i + 1}]
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    #a nuestra lista de opciones le vamos agregar el valor que hemos identificado
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number {i + 1} is NOT FOUND')
                    tries +=1 
                    #refrescamos el navegador
                    driver.refresh()
        #imprimimos las veces que se necesitó para encontrar
        print(f'Finished in {tries} tries')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()