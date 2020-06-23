from selenium import webdriver

# 打开浏览器
def browser():
    driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://192.168.105.117:8090/login')
    dr.quit()

