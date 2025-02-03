# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# # Set up ChromeDriver
# service = Service("/usr/local/bin/chromedriver")
# driver = webdriver.Chrome(service=service)

# # Open a webpage
# driver.get("https://www.google.com")

# # Print page title
# print("Page Title:", driver.title)

# # Close browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
# options.add_argument("--headless")  #use it later
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--autoplay-policy=no-user-gesture-required")

driver = webdriver.Chrome(options=options)

try:
    # Go to Simplilearn website
    driver.get(
        "https://accounts.simplilearn.com/user/login?redirect_url=https%3A%2F%2Flms.simplilearn.com%2F"
    )
    time.sleep(8)  # Wait for the page to load

    #Login
    email_field = driver.find_element(By.NAME, 'user_login')
    email_field.send_keys("rohitr9832@gmail.com")

    password_field = driver.find_element(By.NAME, 'user_pwd')
    password_field.send_keys("b1x0h*%V3M")
    time.sleep(4);

    # Click the login button
    login_submit = driver.find_element(By.NAME, 'btnlogin')
    login_submit.click()
    time.sleep(20)

    #Click Continue Learning
    driver.find_element(By.CSS_SELECTOR, "button.btn.prime.custom_button_ep.ng-star-inserted").click()
    time.sleep(10)

    #Click the lesson name on right sidebar
    driver.find_element(By.XPATH, "//p[@class='lesson-topic-tittle' and normalize-space(text())='5.1 Learning Objectives']").click()
    time.sleep(5)

    # At this point, the video should be playing.
    # The script won't exit, so it will stay connected as long as it's running.

    while True:
        # This loop keeps the script running so the browser stays active
        time.sleep(20)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
