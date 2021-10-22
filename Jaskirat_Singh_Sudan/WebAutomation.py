
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.youtube.com/")
#driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
# driver.implicitly_wait(5)
sleep(5)
searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/paper-item')
searchbox.click()
searchbox.send_keys("Unbox Tharapy")

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#searchbutton.click()