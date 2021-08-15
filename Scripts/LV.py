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

persons = []

#Access webpage and accept cookies
driver.get("https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052674622")
driver.implicitly_wait(10)
#driver.find_element_by_xpath('//*[@class="ucm-button ucm-button--default ucm-choice__yes"]').click()

print(driver.page_source)

# try:
#     element = WebDriverWait(driver, 20).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, "productListingPage-results"))
#     )

#     #Main script
#     for person in driver.find_elements_by_class_name('productListingPage-results'):
#         title = person.find_element_by_xpath('./h3[@class="productCard-productName"]').text
#         #company = person.find_element_by_xpath('./span[@class="lv-product-card__price body-xs"]/a').text
#         #persons.append({'name': title, 'price': company})
#         persons.append({'name': title})
#         print(title)
        
# finally:
#     driver.quit()

# print(persons)

# bags = driver.find_elements_by_xpath('//*[@class="lv-product-card__price body-xs"]')
# for bag in bags:   
#     print(bag.text)
#     txt = [x.text for x in text_element]
#     print(txt, '\n')
#     txt2 = [x.text for x in text_element2]
#     print(txt2, '\n')
#     results_list.append(txt + txt2)
