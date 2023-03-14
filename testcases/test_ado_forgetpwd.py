# -*- coding:utf-8 -*-

import unittest
import time
from config.wddriver import desired_caps
from appium import webdriver
from page.adolescent_model import Adolescent_Model


class TestAdoForget(unittest.TestCase):
    """青少年模式--忘记密码"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.ado = Adolescent_Model(ios_driver)

    def test_ado_frogetpwd(self):
        """
        退出青少年模式--忘记密码
        ：return：
        """
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.forget_pwd_button().click()  # 忘记密码
        self.ado.cancel_call_button().click()  # 联系客服-取消
        self.ado.adolescent_back().click()
        self.ado.adolescent_back().click()  # 返回到青少年首页
