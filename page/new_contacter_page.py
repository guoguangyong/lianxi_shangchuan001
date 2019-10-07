from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class New_Contacter_Info(BaseAction):

    new_contacter_name = By.XPATH,"//*[@text='姓名']"

    new_contacter_phone = By.XPATH,"//*[@text='电话']"

    save_but = By.CLASS_NAME,"android.widget.ImageButton"

    def input_contacter_name(self,name):
        self.input(self.new_contacter_name,name)

    def input_contacter_phone(self,phone_num):
        self.input(self.new_contacter_phone,phone_num)

    def click_save_but(self):
        self.click(self.save_but)

