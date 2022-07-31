from time import sleep

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Install Chrome Driver for Selenium

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

# Main URL

site_URL = 'https://mfnd.similarity.eu/'
driver.get(site_URL)

# Opening File 2 Images

file2_xpath = '//*[@id="view2"]/a'
driver.find_element_by_xpath(file2_xpath).click()
sleep(2)

# Downloading File 2 Images

# Number of images in the folder is 3825 and each page has 10 images
for i in range(3825 // 10):
    li = driver.find_elements_by_tag_name('img')
    for i in li:
        print(i.get_attribute('src'))

    # Last 3 images are thumbnails and are not needed
    for i in li[:-3:]:
        url = i.get_attribute('src')
        print(url)
        filename = url.split('/')[-1]
        print(filename)
        img_data = requests.get(url, allow_redirects=True).content
        # Saved in subfolder 'images'
        open('images/' + filename, 'wb').write(img_data)

    # Clicking on the next page

    try:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/img').click()
        sleep(2)
    except:
        driver.quit()
