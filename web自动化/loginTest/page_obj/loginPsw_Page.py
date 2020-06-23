# 创建登录页面对象，对用户登录页面上的用户名/密码输入框、登录按钮和
# 提示信息等元素的定位进行封装。
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_obj.base import Page


class login(Page):
    # 用户登录界面
    url = '/login'
    # 定位用户名
    login_username_loc = (By.ID, 'normal_login_accountNo')
    # 定位密码框
    login_password_loc = (By.ID, 'normal_login_password')
    # 登录按钮的定位
    login_button_loc = (By.CSS_SELECTOR, 'button[class^="ant-btn"]')
    # 登录报错信息的定位
    login_error_loc = (By.XPATH, '//*[@id="normal_login"]/div[1]/div/div[2]/div')
    # 登录成功用户名信息
    login_name_success_loc = (By.XPATH, '//*[@id="root"]/section/header/div[3]/div[2]/div/span[2]')

    # 登录成功手机号
    login_phone_success_loc = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[2]')

    # 选择密码登录
    def login_ByPsd(self):
        self.driver.find_element_by_css_selector('.BlackColor___1F88e').click()

    # 用户名输入
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 密码输入
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 点击登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一密码登录入口
    def user_login(self, username='18351952332', password='1996xh729'):
        self.open()
        self.login_ByPsd()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    # 登录错误提示信息
    def login_errot_hint(self):
        return self.find_element(*self.login_error_loc).text

    # 登录成功提示信息
    def login_user_success(self):
        # 鼠标悬停在用户名上
        name = self.find_element(*self.login_name_success_loc)
        ActionChains(self.driver).move_to_element(name).perform()
        sleep(2)
        username = self.find_element(*self.login_phone_success_loc).text
        username = username.strip('账号：')
        return username


