from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from socket import socket
import time
import json
import random
from tqdm import tqdm
hashtags = [
            "lgbt",
            "queer",
            "lgptq+",
            "lgbtqplus",
            "gleichberechtigung",
            "genderpaygap",
            "gaycommunity",
            "alternativekinderbücher",
            "sexismus",
            "feminism",
            "traumatabewältigung",
            "geschlechtsnormen",
            "geschlechternormen",
            "bücher"]
comment = ["Starker Beitrag 👍"]


class InstagramBot:

    def __init__(self, username, password):
        data = None
        with open('settings.json', 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        self.username = obj['instagram']['user']
        self.password = obj['instagram']['pass']
        #self.driver = webdriver.Firefox()
        # fireFoxOptions = webdriver.FirefoxOptions()
        # fireFoxOptions.set_headless()
        # self.driver = webdriver.Firefox(firefox_options=fireFoxOptions)

        options = Options()
        # options.headless = True
        self.driver = webdriver.Firefox(options=options)

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
        driver.get(
            "https://www.instagram.com/accounts/login/?source=auth_switcher/")
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher/']")
        # login_button.click()
        time.sleep(2)
        user_name_element = driver.find_element_by_xpath(
            "//input[@name='username']")
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
        for i in range(1, 5):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        hrefs = driver.find_elements_by_tag_name("a")
        all_links = []
        counter = 0
        for link in hrefs:
            all_links.append(link.get_attribute("href"))

        # pic_hrefs = [hrefs.get_attribute("href") for elem in hrefs]
        #pic_hrefs = [href for href in all_links if hashtag in href]
        # print(hashtag + 'hat' +  str(len(all_links) + 'Fotos zum Liken'))
        all_links = all_links[10:-14]
        # print(all_links)
        # print(pic_hrefs)
        counter = 0
        for pic_href in all_links:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                # driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                driver.find_element_by_class_name("wpO6b").click()
                print('Liked ' + pic_href + ' !')
                y = random.randint(0, 2)
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.click()
                commentArea = driver.find_element_by_class_name('Ypffh')
                commentArea.send_keys(comment[0])
                time.sleep(1)
                commentButton = driver.find_element_by_class_name('X7cDz')
                time.sleep(2)
                commentButton.submit()
                print('Commented ' + str(comment[0]))
                counter += 1
                print(counter)
                x = random.randint(55, 75)
                print('waiting ' + str(x) + ' seconds')
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(x/10)
                        pbar.update(10)
                if counter == len(all_links):
                    print("DONE")
            except Exception as e:
                time.sleep(2)
                print('notliked')
                print(e)


DNS = InstagramBot("username", "password")
DNS.login()
for hashtag in hashtags:
    DNS.like_photo(hashtag)
