import time
class class_Login_page:
    def __init__(self,driver):
        self.driver = driver
    def Username(self,user_name):
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user_name)
    def Password(self, pass_word):
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(pass_word)
    def Login(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()