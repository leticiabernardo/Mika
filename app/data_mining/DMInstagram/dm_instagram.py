from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
from app.file_manager.make_txt import MakeTxt
import config


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = self.configure_webdriver()
        self.make_txt = MakeTxt()

    @staticmethod
    def configure_webdriver():
        if platform.system() == 'Windows':
            # ChromeDriver 2.41
            # https://chromedriver.storage.googleapis.com/index.html?path=2.41/
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Python\chromedriver.exe")
        else:
            # Geckodriver
            driver = webdriver.Firefox()

        driver.maximize_window()
        return driver

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(4)

        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/']")
        login_button.click()
        time.sleep(2)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        user_password_elem = driver.find_element_by_xpath("//input[@name='password']")
        user_password_elem.clear()
        user_password_elem.send_keys(self.password)
        user_password_elem.send_keys(Keys.RETURN)
        # enter in field

        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)

        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            element_links = driver.find_elements_by_tag_name('a')
            links_pic_href = [elem.get_attribute('href') for elem in element_links]
            links_pic_href = [href for href in links_pic_href if hashtag in href]

            for pic_href in links_pic_href:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                try:
                    driver.find_element_by_class_name('coreSpriteHeartOpen').click()
                    time.sleep(8)
                except Exception as e:
                    print("Error:", e)
                    time.sleep(2)

    def unfollow(self):
        driver = self.driver
        driver.get('https://www.instagram.com/' + self.username + '/')
        time.sleep(2)

        login_button = driver.find_element_by_xpath("//a[@href='/" + self.username + "/following/']")
        login_button.click()
        time.sleep(2)
        links_unfollow = driver.find_elements_by_css_selector("li.NroHT > div.ywte8")

        users_unfollowing = []
        list_of_unable_unfollow = config.INSTA_UNFOLLOW_DISABLED

        for link_unfollow in links_unfollow:
            username_following = link_unfollow.find_element_by_css_selector("div.gdFJk > div a").text

            if username_following not in list_of_unable_unfollow:
                link_unfollow.find_element_by_css_selector("div.BW116 button").click()

                try:
                    driver.find_element_by_xpath("//button[text()='Deixar de seguir']").click()
                    users_unfollowing.append(username_following)
                    time.sleep(4)
                except Exception as e:
                    print("Error:", e)
                    time.sleep(2)

                    # self.make_txt.save_data("instagram_unfollows", '\n'.join(users_unfollowing))

    def follow_by(self, user_same_followers):
        driver = self.driver

        driver.get('https://www.instagram.com/' + user_same_followers + '/')
        time.sleep(2)

        login_button = driver.find_element_by_xpath("//a[@href='/" + user_same_followers + "/followers/']")
        login_button.click()
        time.sleep(2)
        driver.execute_script("document.getElementsByClassName('j6cq2')[0].scroll(0,900)")
        driver.execute_script("document.getElementsByClassName('j6cq2')[0].scroll(0,900)")
        time.sleep(2)
        links_unfollow = driver.find_elements_by_css_selector("li.NroHT > div.ywte8")

        users_following = []

        for link_unfollow in links_unfollow:
            username_following = link_unfollow.find_element_by_css_selector("div.gdFJk > div a").text

            button_action = link_unfollow.find_element_by_css_selector("div.BW116 button")

            if button_action.text == 'Seguir':
                button_action.click()
                users_following.append(username_following)

                time.sleep(4)

    def close_driver(self):
        driver = self.driver
        driver.quit()


instagramTest = InstagramBot(config.INSTA_USERNAME, config.INSTA_PASSWORD)
instagramTest.login()
[instagramTest.follow_by(tag) for tag in config.INSTA_COPY_FOLLOWERS_BY]
[instagramTest.like_photo(tag) for tag in config.INSTA_TAGS_FOLLOW]
instagramTest.close_driver()
