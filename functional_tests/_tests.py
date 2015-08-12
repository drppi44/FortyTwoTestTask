import time
from apps.hello.models import MyData
from django.test import LiveServerTestCase
from selenium import webdriver


class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_home_page_has_data(self):
        self.browser.get(self.live_server_url)

        my_data = MyData.objects.first()
        table_text = self.browser.find_element_by_id('data_table').text

        self.assertIn(my_data.name, table_text)
        self.assertIn(my_data.last_name, table_text)
        self.assertIn(my_data.bio, table_text)
        self.assertIn(my_data.email, table_text)
        self.assertIn(my_data.jabber, table_text)
        self.assertIn(my_data.skype, table_text)
        self.assertIn(my_data.other_contacts, table_text)


class RequestPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_requests_link_on_home_page_works(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_css_selector('a').click()

        title = self.browser.find_element_by_css_selector('h3').text

        self.assertIn('Midleware', title)
