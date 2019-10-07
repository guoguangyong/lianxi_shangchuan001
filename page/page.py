from page.contacter_list_page import New_Contacter
from page.new_contacter_page import New_Contacter_Info


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def new_build_contacter_but(self):
        return New_Contacter(self.driver)

    @property
    def input_contacter_info(self):
        return New_Contacter_Info(self.driver)