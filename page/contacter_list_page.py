from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class New_Contacter(BaseAction):

    new_build_contacter_but = By.ID,"com.android.contacts:id/floating_action_button"

    def click_new_contacter_but(self):
        self.click(self.new_build_contacter_but)