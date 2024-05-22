from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from seleniumbase import get_driver

import time

# assert "Python" in driver.title
# print(DesiredCapabilities)


def login_user():
    driver.maximize_window()
    driver.get("http://localhost:3000/")
    assert "Bloggerline" in driver.title
    time.sleep(2)
    elem = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[1]/div[3]/ul/li[1]/a')
    print(elem)
    elem.click()
    username = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/form/input[1]')
    username.send_keys("gg2")
    password = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/form/input[2]')
    password.send_keys("gg")
    submitBtn = driver.find_element(By.CLASS_NAME, 'loginButton')
    submitBtn.click()
    time.sleep(2)
    assert "No results found." not in driver.page_source
    # driver.close()


def write_post_and_delete():
    elem = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[1]/div[2]/ul/li[2]/a')
    elem.click()
    time.sleep(2)
    tag_filed = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/form/div[1]/div/div[2]/input')
    tag_filed.send_keys('TestTag')
    tag_filed.send_keys(Keys.RETURN)
    title_filed = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/form/div[1]/input[2]')
    title_filed.send_keys("Test title from Selenium")
    story_text = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/form/div[2]/textarea')
    story_text.send_keys("This is a test post made with selenium web driver")
    submit_button = driver.find_element(By.CLASS_NAME, 'writeSubmit')
    submit_button.click()
    time.sleep(3)
    delete_post = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/h1/div/i[2]')
    delete_post.click()
    time.sleep(2)
    logout_button = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[1]/div[2]/ul/li[3]')
    logout_button.click()
    time.sleep(2)
    driver.close()


# Run tests
if __name__ == "__main__":
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    login_user()
    write_post_and_delete()

    driver = get_driver("firefox", headless=False)
    print(driver)
    login_user()
    write_post_and_delete()

    driver = get_driver("edge", headless=False)
    print(driver)
    login_user()
    write_post_and_delete()
    # pass
