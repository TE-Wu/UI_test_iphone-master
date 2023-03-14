# -*- coding:utf-8 -*-

import unittest
import time
from config.wddriver import desired_caps
from appium import webdriver
from page.adolescent_model import Adolescent_Model


class TestAdoReset(unittest.TestCase):
    """青少年模式--重置密码"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.ado = Adolescent_Model(ios_driver)

    def test_ado_resetpwd(self):
        """
        退出青少年模式--重置密码
        ：return：
        """
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.reset_pwd_button().click()  # 重置青少年密码
        self.ado.original_pwd().send_keys("5555")  # 输入原密码
        self.ado.new_pwd().send_keys("1111")  # 输入新密码
        self.ado.again_pwd().send_keys("1111")  # 确认新密码
        self.ado.out_pwd().send_keys("1111")  # 退出密码
