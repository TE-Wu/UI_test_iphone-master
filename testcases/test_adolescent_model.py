# -*- coding:utf-8 -*-

import unittest
import time
from config.wddriver import desired_caps
from appium import webdriver
from page.adolescent_model import Adolescent_Model


class TestAdoModel(unittest.TestCase):
    """青少年模式设置"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.ado = Adolescent_Model(ios_driver)

    def test_ado_model(self):
        """
        首次启动--模式选择--已设置密码
        :return:
        """
        self.ado.teenagers_button().click()  # 进青少年模式
        # self.ado.standard_button().click()  # 进标准模式
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.out_pwd().send_keys("5555")  # 退出密码

    def test1_ado_model(self):
        """
        首次启动--模式选择--未设置密码
        :return:
        """
        self.ado.teenagers_button().click()  # 进青少年模式
        self.ado.set_password()
        self.ado.set_pwd().send_keys("5555")  # 设置密码
        self.ado.confirm_password()
        self.ado.set_pwd().send_keys("5555")  # 确认密码
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.out_pwd().send_keys("5555")  # 退出密码
