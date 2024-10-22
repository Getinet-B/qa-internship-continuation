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
from pages.right_number_ui_elements_page import RightNumberUiElementsPage
#from pages.sd_want_to_sell_option_page import FilterSecondaryDeals
from pages.sd_want_to_buy_option_page import FilterWantToBuyOption
from pages.secondary_deals_pagination_page import SecondaryDealsPaginationPage
from pages.settings_page import SettingsPage
from pages.subscription_and_payments_page import OpenSubscriptionPaymentPage
from pages.whatsapp_and_telegram_communities_page import AccessWhatsappTelegramCommunitiesPage


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
        self.right_number_ui_elements_page = RightNumberUiElementsPage(driver)
        #self.sd_want_to_sell_option_page = FilterSecondaryDeals(driver)
        self.sd_want_to_buy_option_page = FilterWantToBuyOption(driver)
        self.secondary_deals_pagination_page = SecondaryDealsPaginationPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscription_and_payments_page = OpenSubscriptionPaymentPage(driver)
        self.whatsapp_and_telegram_communities_page = AccessWhatsappTelegramCommunitiesPage(driver)

