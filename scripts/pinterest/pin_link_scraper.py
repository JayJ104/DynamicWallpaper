from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from PIL import Image

def get_all_pin_urls(search_keys: dict):
    all_pin_urls = {}

    #Pinterest credentials
    username = "gdscteameve@gmail.com"
    password = "teameve123"

    # instance of Chrome WebDriver
    driver = webdriver.Chrome()

    # login
    driver.get("https://www.pinterest.com/login/")
    time.sleep(5)
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR , "button[type='submit']").click()
    time.sleep(5)

    # search
    for id in search_keys:
        query = search_keys[id] + " aesthetic"
        query = query.replace(" ", "%20")
        search_url = f"https://www.pinterest.com/search/pins/?q={query}"
        driver.get(search_url)
        time.sleep(5)

        pin_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='pinWrapper'] img")
        pin_urls = [element.get_attribute("src") for element in pin_elements]
        
        all_pin_urls[id] = pin_urls


    # Close the browser
    driver.quit()

    return all_pin_urls

import requests


def download(url_list, output_folder):
    for url in url_list:
        try:
            filepath = output_folder + str(url_list.index(url)) + ".jpg"
            urllib.request.urlretrieve(url, filepath)
        except Exception as e:
            print(f"An error occurred: {e}")


# def download_this_image():
#     try:
#         filepath = "image.jpg"
#         urllib.request.urlretrieve("https://i.pinimg.com/736x/bb/bc/a4/bbbca4d06a901d604c54c3c8adaab67d.jpg", filepath)
#     except Exception as e:
#         print(f"An error occurred: {e}")


