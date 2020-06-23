from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get('http://192.168.105.117:8090/login')
sleep(3)
url = driver.current_url
print(url)

# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.find_element_by_css_selector('.BlackColor___1F88e').click()
# driver.find_element_by_css_selector('#normal_login_accountNo').send_keys('18351952332')
# driver.find_element_by_css_selector('#normal_login_password').send_keys('1996xh729')
#
# driver.find_element_by_css_selector('button[class^="ant-btn"]').click()
# sleep(3)
# name = driver.find_element_by_xpath('//*[@id="root"]/section/header/div[3]/div[2]/div/span[2]')
# ActionChains(driver).move_to_element(name).perform()
# sleep(5)
# phone = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[2]').text
#
# print(phone)

driver.quit()


