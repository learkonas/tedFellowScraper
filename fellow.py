from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

options = Options() 
options.headless = True # Opens browser in background
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)  # wait up to 10 seconds

with open('fellows.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for page in range(1, 18):
        url = f'https://www.ted.com/people/fellows?page={page}'
        driver.get(url)

        # Find all <a> tags with the specified class
        a_tags = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.results__result.media.media--sm-v.m4")))

        # Extract the href attribute from each <a> tag
        hrefs = [a.get_attribute('href') for a in a_tags]

        # Extract the number from each href and write it to the CSV file
        for href in hrefs:
            number = href.split('/')[-2]
            print(number)
            writer.writerow([number])
        time.sleep(4)

driver.quit()