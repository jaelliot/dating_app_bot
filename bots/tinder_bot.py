from selenium.webdriver.common.keys import Keys
from time import sleep
from login_details import EMAIL, PASSWORD
from .base_bot import BaseBot


class TinderBot(BaseBot):
    def open_app(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        login = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
        sleep(1)
        self.login()

        sleep(6)
        self.handle_popups()

    def login(self):
        login_with_facebook = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_with_facebook.click()
        
        sleep(2)
        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_popup_window)

        cookies_accept_button = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
        cookies_accept_button.click()

        email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pw_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_button = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        email_field.send_keys(EMAIL)
        pw_field.send_keys(PASSWORD)
        login_button.click()
        self.driver.switch_to.window(base_window)

    def handle_popups(self):
        try:
            allow_location_button = self.driver.find_element('xpath', '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
            allow_location_button.click()
        except:
            print('No location popup')

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
            notifications_button.click()
        except:
            print('No notification popup')

    def right_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_RIGHT)
    
    def left_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.right_swipe()
            except:
                self.close_match()

    def close_match(self):
        match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def get_matches(self):
        match_profiles = self.driver.find_elements('class name', 'matchListItem')
        message_links = []
        for profile in match_profiles:
            href = profile.get_attribute('href')
            if href not in ['https://tinder.com/app/my-likes', 'https://tinder.com/app/likes-you']:
                message_links.append(href)
        return message_links

    def send_messages_to_matches(self):
        links = self.get_matches()
        for link in links:
            self.send_message(link)

    def send_message(self, link):
        self.driver.get(link)
        sleep(2)
        text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
        text_area.send_keys('hi')
        text_area.send_keys(Keys.ENTER)
