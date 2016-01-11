import time
from apps.hello.models import UserProfile
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from apps.hello.models import MyHttpRequest


class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_home_page_has_data(self):
        """home page contains table with UserProfile"""
        self.browser.get(self.live_server_url)

        my_data = UserProfile.objects.first()
        table_text = self.browser.find_element_by_css_selector(
            '.personal-info').text

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

    def test_requests_page_updates_requests(self):
        """/request/ page updates is_viewed in 5 seconds if active"""
        for i in range(5):
            self.client.get(self.live_server_url + reverse('index'))

        self.browser.get(self.live_server_url + reverse('request'))
        time.sleep(1)

        elements = self.browser.find_elements_by_class_name('is_viewed')
        for element in elements:
            self.assertEquals(element.text, 'False')

        self.assertIn(
            '(%d)' % MyHttpRequest.objects.filter(is_viewed=False).count(),
            self.browser.title
        )

        time.sleep(5)

        elements = self.browser.find_elements_by_class_name('is_viewed')
        for element in elements:
            self.assertEquals(element.text, 'True')
        self.assertIn(
            '(%d)' % MyHttpRequest.objects.filter(is_viewed=False).count(),
            self.browser.title
        )


class EditPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_edit_page_can_edit_data(self):
        """ edit page can edit data"""
        self.browser.get(self.live_server_url+reverse('login'))
        self.browser.find_element_by_id('id_username').send_keys('admin')
        self.browser.find_element_by_id('id_password').send_keys('admin')
        self.browser.find_element_by_id('loginForm').submit()

        self.browser.get(self.live_server_url+reverse('edit'))

        self.browser.find_element_by_id('id_name').clear()
        self.browser.find_element_by_id('id_name').send_keys('admin')
        self.browser.find_element_by_css_selector('input[type=submit]').click()

        time.sleep(1)

        self.assertEquals(
            'admin',
            UserProfile.objects.first().name
        )
