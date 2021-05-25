from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



class HMRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('https://www2.hm.com/pl_pl/index.html')

    def tearDown(self):
        self.driver.quit()

    def testInvalidEmail(self):
        driver = self.driver
        login_btn = driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li[1]/div/a[1]')
        login_btn.click()
        time.sleep(5)

        join_btn = driver.find_element_by_xpath('/html/body/div[10]/div/div/button')
        join_btn.click()
        time.sleep(5)

        email = driver.find_element_by_name('email')
        email.send_keys('xxxxx')


        password = driver.find_element_by_name('pwd')
        password.send_keys('Abcdef123!')


        date_day = driver.find_element_by_xpath('//*[@id="modal-signin-day"]')
        date_day.send_keys('05')
        date_month = driver.find_element_by_xpath('//*[@id="modal-signin-month"]')
        date_month.send_keys('07')
        date_year = driver.find_element_by_xpath('//*[@id="modal-signin-year"]')
        date_year.send_keys('1996')
        time.sleep(5)


        registr_btn = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/form/button')
        registr_btn.click()
        registr_btn.location_once_scrolled_into_view
        time.sleep(2)

        scroll_up = driver.find_element_by_xpath('//*[@id="modal-signin-email"]')
        scroll_up.location_once_scrolled_into_view
        time.sleep(2)

        errors = driver.find_elements_by_xpath('//*[@id="modal-signin-email-email-format-error"]')
        visible_error = []
        for error in errors:
            if error.is_displayed():
                visible_error.append(error)

        print("Tekst bledu: ", visible_error[0].text)


if __name__ == "__main__":
    unittest.main()
