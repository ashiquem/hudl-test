from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from pages.loginPage import LoginPage
from pages.uploadPage import UploadPage

import unittest
import config
import os

class UploadShareVideoTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(config.DRIVER_PATH)
        self.driver.maximize_window()
        self.login(self.driver)

    def login(self,driver):
        driver.get(config.LOGIN_URL)
        
        login_page = LoginPage(driver)

        login_page.email_field.send_keys(Keys.CLEAR)
        login_page.email_field.send_keys(config.USER_NAME)

        login_page.password_field.send_keys(Keys.CLEAR)
        login_page.password_field.send_keys(config.PASSWORD)

        login_page.login_button.click()

        WebDriverWait(driver,10).until(EC.title_contains("Home"),message="Login Failed")

    def upload_video(self,driver,file_path):
        driver.get(config.UPLOAD_URL)

        upload_page = UploadPage(driver)
        upload_page.select_files_button.send_keys(file_path)
        

        class header_has_text(object):

            def __init__(self, text):
                self.text = text
        
            def __call__(self, driver):
                upload_page = UploadPage(driver)
                upload_header = upload_page.upload_header
                
                if upload_header.text == "Upload Complete":
                    return True
                else:
                    return False

        WebDriverWait(driver,config.UPLOAD_TIMEOUT).until(header_has_text("Upload Complete"),message="Upload failed")

    def share_video(self,driver):
        upload_page = UploadPage(driver)
        upload_page.edit_share_button.click()

        self.assertIn("All Team",driver.page_source)
        upload_page.save_button.click()


    def test_share_uploaded_video(self):
        driver = self.driver
        self.upload_video(driver,os.getcwd()+ config.VIDEO_FILE)
        self.share_video(driver)
        
        
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
