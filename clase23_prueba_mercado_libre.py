from itertools import product
import unittest
from selenium import webdriver
from time import sleep

class PruebaTecnica(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        #driver.get('https://www.mercadolibre.com')
        driver.get('https://www.google.com')

    def test_mercado_libre(self):
        
        input_field = self.driver.find_element_by_name('q')
        search_page = 'Mercado libre'
        input_field.send_keys(search_page)
        input_field.submit()

        find_option = self.driver.find_element_by_partial_link_text('Mercado Libre Colombia - Envíos Gratis en el día')
        find_option.click()
        
        #country = self.driver.find_element_by_id('CO')
        #country.click()

        #search_product = self.driver.find_element_by_class_name('nav-search-input')
        search_product = self.driver.find_element_by_name('as_word')
        name_product = 'Playstation 4'
        search_product.send_keys(name_product)
        search_product.submit()

        #condition = self.driver.find_element_by_css_selector('#root-app > div > div.ui-search-main.ui-search-main--exhibitor.ui-search-main--only-products > aside > section > div:nth-child(3) > ul > li:nth-child(1) > a > span.ui-search-filter-name')
        state_product = self.driver.find_element_by_partial_link_text('Nuevo')
        state_product.click()
        sleep(5)

        #city = self.driver.find_element_by_link_text('#root-app > div > div.ui-search-main.ui-search-main--exhibitor.ui-search-main--only-products > aside > section.ui-search-filter-groups > div:nth-child(3) > ul > li:nth-child(1) > a > span.ui-search-filter-name')
        city = self.driver.find_element_by_partial_link_text('Bogotá D.C.')
        city.click()
        sleep(5)

        order_menu = self.driver.find_element_by_class_name('andes-dropdown__display-values')
        order_menu.click()
        sleep(5)

        order_price = self.driver.find_element_by_css_selector('#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        order_price.click()
        sleep(5)

        #name_article = self.driver.find_element_by_class_name('ui-search-item__title')
        #name_article.click()

        #vamos a colocar los productos dentro de una lista
        articles = []
        prices = []

        for i in range(5):
            article_name = self.driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = self.driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)
        print(articles, prices)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
