import unittest
from selenium import webdriver #para comunicarnos con el navegador

class HelloWorldTwo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'E:\descargas\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #maximizar la ventana por si hay elementos responsivos
        driver.maximize_window()
        #los segundos de espera de la ventana
        driver.implicitly_wait(15)

    #lo va buscar por el campo de busqueda por el id
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
    #lo va buscar por el nombre del campo
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    #lo va buscar por el nombre de la clase
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
    #va buscar el número de imagenes
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))
    
    #def test_vip_promo(self):
    #faltó la ruta del xpath
    #    vip_promo = self.driver.find_element_by_xpath('')
    #lo va buscar por el xpath
    def test_shopping_cart_icon(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main(verbosity=2)