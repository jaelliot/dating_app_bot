from selenium import webdriver
from abc import ABC, abstractmethod


class BaseBot(ABC):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    @abstractmethod
    def open_app(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def auto_swipe(self):
        pass

    @abstractmethod
    def send_messages_to_matches(self):
        pass
    
    def close(self):
        self.driver.quit()
