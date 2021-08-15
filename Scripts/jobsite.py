from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=r"c:\temp\chromedriver.exe")
driver.get("https://uk.indeed.com/")
search = driver.find_element_by_id("text-input-what")
search.send_keys("automation engineer")
search = driver.find_element_by_id("text-input-where")
search.send_keys("London, Greater London")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mosaic-zone-jobcards"))
    )
    print(main.text)

    jobs = main.find_elements_by_tag_name("")

finally:
    driver.quit()

# main = driver.find_element_by_id("mosaic-zone-jobcards")
print(main.text)

driver.quit()