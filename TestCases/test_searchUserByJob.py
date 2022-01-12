from PageObjects.CloudLoginPage import LoginPage
from PageObjects.ProjectPage import ProjectPage
from Utilities.readProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from PageObjects.ScanPage import ScanPage
from PageObjects.SearchUserPage import SearchUser
import time


class Test_013_SearchUserByJob:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchUserByJob(self, setup):
        self.logger.info("*********** Test_013_SearchUserByJob ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful **************")

        self.logger.info("***************  Search User By Job **************")
        searchuser = SearchUser(self.driver)
        self.driver.implicitly_wait(30)
        searchuser.clickOnAccountdropdown()

        self.driver.implicitly_wait(30)
        searchuser.clickOnAdvanceViewButtonON()

        time.sleep(5)
        searchuser.clickOnUser()
        time.sleep(5)

        self.driver.implicitly_wait(30)
        searchuser.setJob("Test Engineer")
        time.sleep(5)
        status = searchuser.searchUserByJob("Test Engineer")
        time.sleep(5)
        assert True == status
        self.logger.info("********************  Test_013_SearchUserByJob **********************")
