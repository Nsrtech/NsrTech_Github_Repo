import time
from selenium.webdriver.common.keys import Keys

class Login_page_cls:
    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,username):
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(username)
    def Enter_Password(self,password):
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
    def Click_Login_Button(self):
        self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
    def Verify_Login_Success(self,expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Expected URL:{expected_url}"
    def Add_Employee(self,first_name,middle_name,last_name,employee_id):
        #Navigating to "PIM" module
        self.driver.find_element_by_xpath("//a[normalize-space()='PIM']").click()
        time.sleep(3)
        #navigating to "Add Employee" tab
        self.driver.find_element_by_xpath("//a[normalize-space()='Add Employee']").click()
        time.sleep(3)
        #Entering employee details.
        self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys(first_name)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Middle Name']").send_keys(middle_name)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys(last_name)
        time.sleep(2)

        empid = self.driver.find_element_by_xpath("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.driver.execute_script("arguments[0].value='';", empid)
        empid.send_keys(Keys.CONTROL + "a")  # Select all text
        empid.send_keys(Keys.BACKSPACE)

        empid.send_keys(employee_id)

        time.sleep(2)
        self.driver.find_element_by_xpath("//button[normalize-space()='Save']").click()
        time.sleep(2)


