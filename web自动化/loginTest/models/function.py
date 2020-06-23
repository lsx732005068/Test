import os
import time

from selenium import webdriver

# 封装截图的操作方法
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir).replace("\\", "/")
    currentTime = time.strftime("%Y-%m-%d %H-%M-%S")
    filePath = base_dir + "/result/img/" + currentTime + "_" + file_name
    driver.get_screenshot_as_file(filePath)

if __name__ == '__main__':
		driver = webdriver.Firefox()
		driver.get("http://192.168.105.117:8090/login")
		insert_img(driver, 'login.png')
		driver.quit()
