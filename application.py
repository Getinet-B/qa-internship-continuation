from pages.base_page import BasePage
from pages.add_project_page import AddProjectPage
from pages.connect_the_company_page import ConnectCompanyPage
from pages.change_lang_page import ChangeLangPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.change_password_page import OpenChangePasswordPage
from pages.open_community_page import OpenCommunityPage
from pages.open_contact_us_page import OpenContactUsPage
from pages.user_guide_page import OpenUserGuidePage
from pages.regis_page import RegisPage
from pages.registration_page import RegistrationPage
from pages.settings_page import SettingsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.add_project_page = AddProjectPage(driver)
        self.connect_the_company_page = ConnectCompanyPage(driver)
        self.change_lang_page = ChangeLangPage(driver)
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.change_password_page = OpenChangePasswordPage(driver)
        self.open_community_page = OpenCommunityPage(driver)
        self.open_contact_us_page = OpenContactUsPage(driver)
        self.user_guide_page = OpenUserGuidePage(driver)
        self.regis_page = RegisPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.settings_page = SettingsPage(driver)

