import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        #recibiremos el número de elementos que queremos agregar
        elements_added = int(input("How many elements will you add?: "))
        #recibiremos el número de elementos que queremos eliminar
        elements_removed = int(input("How many elements will you remove?: "))
        #calcularemos la diferencia de los datos que hay
        total_elements = elements_added - elements_removed

        #identificamos la variable donde está el botón para agregar los elementos
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(35)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements the existent")
                break
        if total_elements > 0:
            print(f'The are {total_elements} elements on screen')
        else:
            print(f'There 0 are elements on screen')
        sleep(10)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)