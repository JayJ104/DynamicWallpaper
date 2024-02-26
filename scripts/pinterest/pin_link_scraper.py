from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from PIL import Image
import os

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
        pin_urls = []
        query = search_keys[id] + " aesthetic"
        query = query.replace(" ", "%20")
        search_url = f"https://www.pinterest.com/search/pins/?q={query}"

        try:
            driver.get(search_url)
            time.sleep(10)

            pin_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='pinWrapper'] img")
            pin_urls = [element.get_attribute("src") for element in pin_elements]
        except Exception as e:
            print(f"ERROR: {e}")

        all_pin_urls[id] = pin_urls


    # Close the browser
    driver.quit()

    return all_pin_urls

import requests


def download(all_pin_urls, output_folder):
    downloaded_images = {}
    print("downloading...\n")

    if(not os.path.isdir(output_folder)):
        os.mkdir(output_folder)

    for key in all_pin_urls:
        song_folder = "pins/" + str(key) + "/"
        if(not os.path.isdir(song_folder)):
            os.mkdir(song_folder)

        url_list = all_pin_urls[key]
        downloaded_images[key] = []
        link_count = 0

        for url in url_list:
            if(link_count > 10):
                break
            try:
                filepath = song_folder + str(url_list.index(url)) + ".jpg"
                urllib.request.urlretrieve(url, filepath)
                downloaded_images[key].append(filepath)
                link_count += 1
            except Exception as e:
                print(f"Error: {e}")

    return downloaded_images