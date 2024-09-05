import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope="function")
def datadriven_function_setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        print("Launching Chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser")

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



    yield driver

    # Common teardown logic
    if request.session.login_success == True :
        time.sleep(5)
        driver.find_element_by_xpath("//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
        time.sleep(5)
        driver.quit()
    elif request.session.login_success ==False:
        driver.quit()


@pytest.fixture(scope="session")
def keyword_session_setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        print("Launching Chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser")

    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



    yield driver

    if request.session.login_success == True:
        time.sleep(5)
        driver.find_element_by_xpath("//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
        time.sleep(5)
    elif request.session.login_success ==False:
        driver.quit()



