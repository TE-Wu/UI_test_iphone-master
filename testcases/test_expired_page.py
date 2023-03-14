# -*- coding:utf-8 -*-
import unittest
import time
from config.utils import GetIphone
from config.wddriver import desired_caps
from appium import webdriver
from page.expired_page import Expired_Page
from page.fristhome import HomePage
from page.drama_Drplay import Drama_Drplay
from page.login import Dmo
from page.movie_detail import Movie_Detail
from page.my_home import My_Home
from page.videotab import Video_hall


class Test_Expired_Page(unittest.TestCase):
    """
    过期页
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        ios_driver.implicitly_wait(10)
        self.home = HomePage(ios_driver)
        self.dramadr = Drama_Drplay(ios_driver)
        self.detalis = Movie_Detail(ios_driver)
        self.expored = Expired_Page(ios_driver)
        self.videohall = Video_hall(ios_driver)
        self.loginobj = Dmo(ios_driver)
        self.myhome = My_Home(ios_driver)

    def is_show(self):
        try:
            if self.loginobj.newlogin_button():
                return True
        except:
            return False

    def is_login(self):
        """
        如果进入的页面 有登陆按钮或者输入框 则判断未登陆状态 此时进行登陆
        如果进入的页面 没有则判为已经登陆，此时进行退出登陆
        """
        if self.is_show():
            print('未登陆登陆 过期账号')
            self.loginobj.newlogin_button().click()  # 点击登录注册按钮
            print('输入手机号')
            self.loginobj.phonenum_button().send_keys('14500000465')  # 输入
            print('获取验证码')
            self.loginobj.yanzhengma_button().click()  # 获取验证码
            time.sleep(3)
            code = GetIphone(14500000465).get_code()
            self.loginobj.shuru_button().send_keys(code)
            print('登陆成功，过期页展示')
        else:
            try:
                if self.expored.coming_online():
                    pass
            except:
                print('进入个人中心')
                self.home.my_home().click()
                print('进入我的设置')
                self.myhome.myset().click()
                print('点击退出登陆')
                self.myhome.logout().click()
                self.myhome.logout_in().click()
                self.is_show()

    def test_1(self):

        time.sleep(3)
        print('判断是否已经登陆')
        self.is_login()
        print('用户信息：' + self.expored.user_name() + "--" + self.expored.user_number())

        print('点击用户头像，进入我的过期页')
        self.expored.head_img().click()
        print(
            '用户信息：' + self.expored.my_home_username() + "--" + self.expored.my_home_userlevel() + "--" + self.expored.my_home_endtime())
        self.expored.my_home_back().click()

        print('点击即将上线')
        self.expored.coming_online().click()
        print('进入即将上线列表')

        print('点击返回，回到过期页')
        time.sleep(1)
        self.expored.coming_online_back().click()

        print('点击会员续费，进入续费会员页')
        self.expored.renewal_member().click()
        print('点击返回，回到过期页')
        self.expored.renewal_member_back().click()
        time.sleep(1)

        print('点击南瓜影院，进入放映厅列表')
        self.expored.live_button().click()
        print('点击列表第一位，进入放映厅')
        self.expored.live_opt1().click()
        time.sleep(1.5)
        print('点击返回，回到放映厅列表')
        self.videohall.close_live().click()
        time.sleep(1.5)
        print('点击返回，回到过期页')
        self.expored.live_back().click()
        time.sleep(1.5)

        print('点击用户头像，进入我的过期页')
        self.expored.head_img().click()
        print('点击退出账号')
        self.expored.my_home_out().click()
        print('二级弹窗点击取消')
        self.expored.my_home_out_cannel().click()
        print('二级弹窗点击确认')
        self.expored.my_home_out().click()
        self.expored.my_home_out_true().click()
        print('登陆页面展示')
        self.loginobj.newlogin_button()

