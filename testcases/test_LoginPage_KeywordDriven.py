import time
import pytest
from datetime import datetime
from PageObjects.LoginPage_KeywordDriven import Login_page_cls
from utilities.Read_Excel_Data import Read_Excel_Data
from utilities.Logging import Logs

#Code for to generate log files in Logs folder
logger = Logs.Log_Gen()

#Code for reading the excel file test data from utilities
file_path = r"C:\NSR_Python_Projects\Python_Project_Version2\5_Page_Object_Model_Hybrid_Framework\TestData\Keyword_Login_Data.xlsx"
sheet_name = "Sheet1"
test_data = Read_Excel_Data(file_path,sheet_name)

@pytest.mark.parametrize("keyword,input_data,expected_result", test_data)
def test_Login_Keyword(keyword,input_data,expected_result,keyword_session_setup,request):
    logger.info("**********  Test_002_Login_Keyword **********")
    time.sleep(5)
    driver = keyword_session_setup  # Drivre holding webpage
    time.sleep(5)
    login_obj = Login_page_cls(driver)  # This class display user and pwd and login elements
    logger.info(f"Starting Keyword Driven Test with Actions '{keyword}'.")

    if keyword == "Enter Username":
        username = input_data.strip()
        time.sleep(2)
        login_obj.Enter_Username(username)
        time.sleep(2)
        logger.info("********** Username Entered **********")

    elif keyword == "Enter Password":
        password = input_data.strip()

        time.sleep(3)
        login_obj.Enter_Password(password)
        time.sleep(3)
        logger.info("********** Password Entered **********")

    elif keyword == "Click Login Button":
        login_obj.Click_Login_Button()
        time.sleep(3)
        request.session.login_success = True

    elif keyword == "Verify Login Success":
        expt_url = input_data.strip()
        time.sleep(3)
        login_obj.Verify_Login_Success(expt_url)
        time.sleep(3)

    elif keyword == "Add Employee":
        employees_data = []
        for emp_data in input_data.split(','):
            employees_data.append(emp_data.strip())


        if len(employees_data) == 4:
            Fname,Mname,Lname,Empid = employees_data
            login_obj.Add_Employee(Fname,Mname,Lname,Empid)

            logger.info("********** Employee Added **********")
            dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            time.sleep(3)
            driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\5_Page_Object_Model_Hybrid_Framework\\ScreenShots\\Success\\Employee_Added_Success_{dt}.png")

        else:

            logger.error("********** Invalid input data for Add Employee **********")
            dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            time.sleep(3)
            driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\5_Page_Object_Model_Hybrid_Framework\\ScreenShots\\Success\\Employee_Added_Failed_{dt}.png")


        logger.info(f"Test with action '{keyword}' Completed.")
        logger.info("********** Test_002_Login_Keyword Completed **********")




