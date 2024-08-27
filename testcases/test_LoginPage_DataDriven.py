import time
import pytest
from datetime import datetime
from PageObjects.LoginPage_DataDriven import class_Login_page
from utilities.Read_Excel_Data import Read_Excel_Data
from utilities.Logging import Logs

#Code for to generate log files in Logs folder
Login_logs = Logs.Log_Gen()

#Code for reading the excel file test data from utilities
file_path = r"C:\NSR_Python_Projects\Python_Project_Version2\5_Page_Object_Model_Hybrid_Framework\TestData\DataDriven_Login_Data.xlsx"
sheet_name = "Sheet1"
test_data = Read_Excel_Data(file_path,sheet_name)

#Parameterize the test function with data from the Excel file.
@pytest.mark.parametrize("user_name, pass_word, Exp_result",test_data)
def test_Login(user_name,pass_word,Exp_result,datadriven_function_setup,request):
    Login_logs.info("********** Test_001_DDT_Login ****************")
    Login_logs.info("********** Verifying Login DDT Test **********")
    Login_logs.info(f"Starting DDT-Driven test with Username '{user_name}' and password '{pass_word}'.")

    # This is conftest file method to open browser, and display login page.
    driver = datadriven_function_setup
    time.sleep(5)

    #creating a object(login_page) for Login_page class of Source Package.
    #This class_Login_page class will find username, password and login button elements locators.
    login_page = class_Login_page(driver)
    time.sleep(5)

    login_page.Username(user_name)
    login_page.Password(pass_word)
    login_page.Login()
    time.sleep(5)

    if Exp_result == "Pass":
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        Login_logs.info(f"Login test with username '{user_name}' and password '{pass_word}' Test passed!")

        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\5_Page_Object_Model_Hybrid_Framework\\ScreenShots\\Success\\Login_success_{dt}.png")
        time.sleep(5)
        request.session.login_success = True
    elif Exp_result == "Fail":
        Login_logs.error(f"Login test with username '{user_name}' and password '{pass_word}' Test Passed!")
        request.session.login_success = False

        time.sleep(5)
        dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\5_Page_Object_Model_Hybrid_Framework\\ScreenShots\\Success\\Login_Failed_{dt}.png")
        time.sleep(5)
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/"

    Login_logs.info(f"Test with username '{user_name}' and password '{pass_word}' completed!")
    Login_logs.info("********** Completed Test_001_DDT_Login **********")






