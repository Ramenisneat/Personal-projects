import time

import tweepy
from selenium import webdriver

auth = tweepy.OAuthHandler("PphZsWLEa1sbYKukXcOOznm0U", "5KwUdFOaNyczcKxqUp0hj8W5K8QjDCIKCcf4X1LatXVzT1wB9q")
auth.set_access_token("705964108785459200-fSSlsWXL8OXnQ2KeBlOq4Jx5gi6Jvw9",
                      "WMbyTb8LIdYOindyLnex1UJgPWuM3vKLITmmZCRf5xB1h")
api = tweepy.API(auth)


class BOT:
    def __init__(self):
        self.finished = False
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/login?redirect_after_login=https://developer.twitter.com/en/docs#")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input").send_keys(
            "pixelcrafters7@gmail.com")
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input").send_keys(
            "R0s0me123abc")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div/div/form/div/div[3]/div").click()
        time.sleep(1)
        self.driver.get("https://developer.twitter.com/en/apps")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div/div/div/div[3]/div/div/ul/li/div/div[5]/a/button/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/button/span[1]").click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[1]").click()
        while not self.finished:
            name = input("name:")
            self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/label/div/input").clear()
            self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/label/div/input").send_keys(
                name)
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/form/div[12]/button[2]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/form/div[12]/button[2]").click()
            except:
                self.finished = True


BOT()
msg = input("tweet:")
time.sleep(500)
api.update_status(status=msg)
tweets = api.user_timeline(screen_name="Rahul Myana")
tweet = tweets[0]
url = tweet.id
print(url)
driver = webdriver.Chrome()
driver.get("https://twitter.com/rahul_myana/status/{}".format(url))
