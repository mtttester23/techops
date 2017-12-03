import inspect
import Driver
import time
import helper


class DocumentPage(Driver.Driver):
    # класс содержит методы для работы со страницей

    show_results_btn = "//button[@class='rates-button']"
    get_rate_first_part_of_xpath = "//div[@class='rates-current rates-right']//td[@class='rates-current__table-cell rates-current__table-cell_column_"
    get_rate_second_part_of_xpath = "']//span[@class='rates-current__rate-value']"
    get_result_xpath = "//aside[@class='rates-aside print-invisible']//span[@class='rates-converter-result__total-to']"

    def get_convert_panel_xpath(self, xpath_name):
        dict_of_xpaths = {
            'first_part_of_xpath'   : "//div[@class='rates-container rates-aside__filter']", #this part of xpath narrows the search to the options side bar
            'sum'                   : "//input[@placeholder='Сумма']",
            'converterFrom'         : "//select[@name='converterFrom']/parent::div",
            'converterFromRUB'      : "//select[@name='converterFrom']/parent::div//span[contains(.,'RUB')]",
            'converterFromEUR'      : "//select[@name='converterFrom']/parent::div//span[contains(.,'EUR')]",
            'converterFromUSD'      : "//select[@name='converterFrom']/parent::div//span[contains(.,'USD')]",
            'converterTo'           : "//select[@name='converterTo']/parent::div",
            'converterToRUB'        : "//select[@name='converterTo']/parent::div//span[contains(.,'RUB')]",
            'converterToEUR'        : "//select[@name='converterTo']/parent::div//span[contains(.,'EUR')]",
            'converterToGBP'        : "//select[@name='converterTo']/parent::div//span[contains(.,'GBP')]",
            'sourceCard'            : "//div[@class='rates-aside__filter-block rates-aside__filter-block_mode_converter'][contains(.,'Источник')]//div[@class='kit-radio__text'][contains(.,'Карта Сбербанка')]",
            'sourceAccount'         : "//div[@class='rates-aside__filter-block rates-aside__filter-block_mode_converter'][contains(.,'Источник')]//div[@class='kit-radio__text'][contains(.,'Счет в Сбербанке')]",
            'sourceCash'            : "//div[@class='rates-aside__filter-block rates-aside__filter-block_mode_converter'][contains(.,'Источник')]//div[@class='kit-radio__text'][contains(.,'Наличные')]",
            'timeCurrent'           : "//h6[contains(.,'Время')]/parent::div/parent::div//div[@class='kit-radio__text'][contains(.,'Текущее')]",
            'timeSelect'            : "//h6[contains(.,'Время')]/parent::div/parent::div//div[@class='kit-radio__text'][contains(.,'Выбрать')]",
        }
        return dict_of_xpaths.get('first_part_of_xpath') + str(dict_of_xpaths.get(str(xpath_name)))


    def get_current_page_title(self):
        """ method returns the name/title of the page """
        print('\n' + inspect.stack()[0][3])
        return self.driver.title

    def set_convert_options(self,
                            sum_to_convert=100,
                            convert_from_currency="rub",
                            convert_to_currency="usd",
                            source="card",
                            time="current"):
        print('\n' + inspect.stack()[0][3])

        # insert data into field 'sum'
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath(str('sum'))).clear()
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath(str('sum'))).send_keys(str(sum_to_convert))

        # setting options of converting from currency
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('converterFrom')).click()
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('converterFrom' +
                                                                       convert_from_currency.upper())).click()

        # setting options of converting into currency
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('converterTo')).click()
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('converterTo' +
                                                                       convert_to_currency.upper())).click()

        # setting options of converting source
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('source' + source.capitalize())).click()

        # setting options of converting time
        self.driver.find_element_by_xpath(self.get_convert_panel_xpath('time' + time.capitalize())).click()

    def click_show_result_btn(self):
        print('\n' + inspect.stack()[0][3])
        self.driver.find_element_by_xpath(self.show_results_btn).click()

    def get_current_currency_rate(self, buy_or_sell):
        print('\n' + inspect.stack()[0][3])
        try:
            result = self.driver.find_element_by_xpath(self.get_rate_first_part_of_xpath +
                                              str(buy_or_sell) + self.get_rate_second_part_of_xpath).text
            return helper.convert_str_of_digits_to_float(result)
        except:
            return SystemError

    def get_conversion_result(self):
        print('\n' + inspect.stack()[0][3])
        time.sleep(1)
        result = self.driver.find_element_by_xpath(self.get_result_xpath).text
        return helper.convert_str_of_digits_to_float(result)
