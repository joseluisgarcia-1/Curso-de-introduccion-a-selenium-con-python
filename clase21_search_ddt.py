import unittest, csv
from ddt import ddt, data, unpack
from selenium import webdriver

def file_csv(file_name):
    rows = []
    #abrimos el archivo en modo lectura(r)
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):
    #en la @data están incluidos los términos que vamos a buscar y la cantidad de elementos que esperamos como resultado
    #usamos el @unpcack para desempaquetar la tupla @data y puedan ser consultadas en forma individual
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\Descargas\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(50)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    
    @data(*file_csv('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)
        print(f'found {len(products)} products')
        #print(f"Found {len(products)} products")

        #vamos a imprimir cada uno de los nombres de productos 
        #for product in products:
        #    print(product.text)

        #self.assertEqual(expected_count, len(products))
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()