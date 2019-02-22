class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.email_element_id = "email"
        self.password_element_id = "password"
        self.login_button_id = "logIn"

    @property
    def email_field(self):
        return self.driver.find_element_by_id(self.email_element_id)

    @property
    def password_field(self):
        return self.driver.find_element_by_id(self.password_element_id)

    @property
    def login_button(self):
        return self.driver.find_element_by_id(self.login_button_id)
