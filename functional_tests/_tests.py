import time
from apps.hello.models import MyData
from django.test import LiveServerTestCase
from selenium import webdriver
from apps.t3_middleware.models import MyHttpRequest


class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_home_page_has_data(self):
        """
        home page should contain table with mydata in it
        """
        self.browser.get(self.live_server_url)

        my_data = MyData.objects.first()
        table_text = self.browser.find_element_by_css_selector('.personal-info').text

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
        """
        homepage contains link ot request page (/request/)
        """
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_css_selector('.btn-success').click()

        title = self.browser.find_element_by_css_selector('h1').text

        self.assertIn('Midleware', title)

    def test_requests_page_updates_asynchronously(self):
        """
        when new httprequest comes, request page update its table
        """
        self.browser.get(self.live_server_url+'/request/')

        time.sleep(2)

        table = self.browser.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')

        _count = len(rows)

        self.client.get('/')

        time.sleep(2)

        table = self.browser.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertGreater(len(rows), _count)

    def test_requests_page_title_updates_request_count(self):
        """title on requests page should contain not viewed requests number"""
        self.browser.get(self.live_server_url+'/request/')
        time.sleep(2)

        title_text = self.browser.find_element_by_css_selector('h1').text
        title_text = title_text.split('(')[1]
        request_count_from_template = title_text.split(')')[0]

        not_viewed_request_count = MyHttpRequest.objects.filter(is_viewed=False).count()
        self.assertEquals(int(request_count_from_template), not_viewed_request_count)


class EditPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_login_works(self):
        """user can see login link on main page,
        it redirects to login page"""
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_id('login_button').click()

        login_form = self.browser.find_element_by_id('login_form')

        self.assertTrue(login_form)
