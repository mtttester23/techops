import configparser
import inspect
from selenium import webdriver
import unittest
import DocumentPage


class TestCases(unittest.TestCase):
    """ основной класс, в котором содержатся тест кейсы"""
    configParser = configparser.RawConfigParser()
    # НЕОБХОДИМО ИЗМЕНИТЬ ПУТЬ К configurationfile НА ВАШЕМ КОМПЬЮТЕРЕ
    prodConfigFilePath = r'C:\Users\dupce\Desktop\homework\cp' \
                         r'\configurationfile'
    configParser.read(prodConfigFilePath)
    url_to_go = configParser.get('production', 'link')

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.get(self.url_to_go)

    # переменные используемые в качестве входных данных для тестов
    page_title = "«Сбербанк» - Калькулятор иностранных валют"
    sum_to_convert = 1000

    def make_sure_its_correct_page(self):
        print('\n'+inspect.stack()[0][3])
        assert DocumentPage.DocumentPage(self.driver).get_current_page_title() \
            in self.page_title

    def test001_convert_1000usd_into_rub(self):
        print('\n'+inspect.stack()[0][3])
        self.make_sure_its_correct_page()
        DocumentPage.DocumentPage(self.driver).set_convert_options(
            sum_to_convert=self.sum_to_convert,
            convert_from_currency='usd',
            convert_to_currency='rub',
            source='cash')
        rate = DocumentPage.DocumentPage(self.driver).get_current_currency_rate('buy')
        DocumentPage.DocumentPage(self.driver).click_show_result_btn()
        result = DocumentPage.DocumentPage(self.driver).get_conversion_result()
        first_assert = (float(self.sum_to_convert) * rate)
        second_assert = result
        print("assert " + str(first_assert) + " IN " + str(second_assert))
        assert str(first_assert) in str(second_assert)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
