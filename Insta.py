from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from socket import socket
import time



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    print("""
                 
             ___                       _
            / _ \                     | |
  _ __ ___ | | | |_ __   __ _ _ __ ___| |__
 | '_ ` _ \| | | | '_ \ / _` | '__/ __| '_  |
 | | | | | | |_| | | | | (_| | | | (__| | | |
 |_| |_| |_|\___/|_| |_|\__,_|_|  \___|_| |_|

                                                """)



    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher/']")
        #login_button.click()
        time.sleep(2)
        user_name_element = driver.find_element_by_xpath("//input[@name='username']")
        user_name_element.clear()
        user_name_element.send_keys(self.username)
        pswrd_elem = driver.find_element_by_xpath("//input[@name='password']")
        pswrd_elem.clear()
        pswrd_elem.send_keys(self.password)
        pswrd_elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("https://www.instagram.com")

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        hrefs = driver.find_elements_by_tag_name("a")
        all_links = []
        for link in hrefs:
            all_links.append(link.get_attribute("href"))

        # pic_hrefs = [hrefs.get_attribute("href") for elem in hrefs]
        pic_hrefs = [href for href in all_links if hashtag in href]
        # print(hashtag + 'hat' +  str(len(all_links) + 'Fotos zum Liken'))
        all_links = all_links[:-14]
        # print(all_links)
        # print(pic_hrefs)
        for pic_href in all_links:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//button/span").click()
                print('Liked ' + pic_href + ' !')
                time.sleep(12)
            except Exception as e:
                time.sleep(2)
                print('notliked')

DNS = InstagramBot("digitalnativesquad", "Siedler1208")
DNS.login()
DNS.like_photo(input("Welcher Hashtag? "))
