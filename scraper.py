import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options() 
options.headless = True # Opens browser in background
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 6)  # wait up to 10 seconds

# Open the CSV file in read mode
with open('fellows.csv', 'r') as file:
    reader = csv.reader(file)

    # Open the new CSV file in write mode
    with open('bio.csv', 'w', newline='') as bio_file:
        bio_writer = csv.writer(bio_file)
        bio_writer.writerow(['URL', 'Bio'])  # Write the header

        # Loop over each number in the CSV file
        try:
            for row in reader:
                time.sleep(4)
                number = row[0]
                print(f"Reviewing profile {number}")
                url = f'https://www.ted.com/profiles/{number}/about'
                driver.get(url)
                try: # Find the Bio div and the target div
                    bio_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Bio')]")))
                    target_div = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Bio')]/following-sibling::div[1]")))

                    # Write the URL and bio to the new CSV file
                    bio_writer.writerow([url, target_div.text])
                except Exception as e:
                    print(f"Failed to find bio for URL {url}: {e}")
        except Exception as e:
            print(f"Alas for {url}: {e}")
driver.quit()