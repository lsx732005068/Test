import unittest
from time import sleep

from models import myunit, function
from page_obj.loginPsw_Page import login


class loginTest(myunit.MyTest):
    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    # 用户名密码正确
    def test_login1(self):
        self.user_login_verify('18351952332', '1996xh729')
        sleep(3)
        po = login(self.driver)
        self.assertEqual(po.login_user_success(), u'18351952332')
        function.insert_img(self.driver, "user_pwd_true.png")

    # 用户名密码为空登录
    def test_login2(self):
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.login_errot_hint(), u'请输入手机号!')
        function.insert_img(self.driver, "user_pawd_empty.png")

if __name__ == '__main__':
    unittest.main()


