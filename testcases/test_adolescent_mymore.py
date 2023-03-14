# -*- coding:utf-8 -*-

import unittest
import time
from config.wddriver import desired_caps
from appium import webdriver
from page.adolescent_model import Adolescent_Model
from page.my_home import My_Home
from page.fristhome import HomePage


class TestAdoMymore(unittest.TestCase):
    """个人设置--青少年模式"""

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.ado = Adolescent_Model(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.home = HomePage(ios_driver)

    def test_ado_mymore(self):
        """
        个人中心设置-进青少年模式--已设置密码
        ：return：
        """
        self.home.my_home().click()  # 进个人首页
        self.myhome.myset().click()  # 进设置页
        self.ado.adolescent_button().click()  # 我的设置-青少年模式
        adonotopen = self.ado.not_open().text
        print(f"当前页面：{adonotopen}")
        self.ado.open_baby_button().click()  # 开启青少年模式
        # 获取青少年首页影片信息
        moviename = self.ado.moviename()
        movietype = self.ado.movietype()
        print("影片信息：" + moviename + movietype)
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_type()
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.out_pwd().send_keys("5555")  # 退出密码

    def test1_ado_mymore(self):
        """
        个人中心设置-进青少年模式--未设置密码
        ：return：
        """
        time.sleep(3)
        self.home.my_home().click()  # 进个人首页
        self.myhome.myset().click()  # 进设置页
        self.ado.adolescent_button().click()  # 我的设置-青少年模式
        adonotopen = self.ado.not_open().text
        print(f"当前页面：{adonotopen}")
        self.ado.open_baby_button().click()  # 开启青少年模式
        self.ado.set_password()
        self.ado.set_pwd().send_keys("5555")  # 设置密码
        self.ado.confirm_password()
        self.ado.set_pwd().send_keys("5555")  # 确认密码
        # 获取青少年首页影片信息
        moviename = self.ado.moviename()
        movietype = self.ado.movietype()
        print("影片信息：" + moviename + movietype)
        self.ado.out_adolescent().click()  # 青少年首页-退出
        self.ado.out_type()
        self.ado.out_ado().click()  # 退出青少年模式
        self.ado.out_pwd().send_keys("5555")  # 退出密码
