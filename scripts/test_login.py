import time

from base.base_driver import init_driver
from page.page import Page


class Test_Add_Contacter:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_add_contacter(self):
        self.page.new_build_contacter_but.click_new_contacter_but()
        self.page.input_contacter_info.input_contacter_name("ssssss")
        self.page.input_contacter_info.input_contacter_phone("333333333333")
        self.page.input_contacter_info.click_save_but()