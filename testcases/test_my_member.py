import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.finmreview_detail import Finmreview_Detail
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_member import My_Member
from page.my_movie import My_Movie
from page.video import Video


class Test_My_Member(unittest.TestCase):
    """
    我的会员
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.member = My_Member(ios_driver)

    def test_1(self):

        time.sleep(4)
        print('更多页 点击我的会员')
        self.home.my_home().click()
        self.myhome.member().click()

        print('点击普通会员')
        self.member.ordinary_member_tab().click()
        print('会员信息：' + "" + self.member.username() + "" + self.member.member_end_time())

        print('续费页 会员卡内容展示：'+self.member.member_continuous()+"--"+self.member.member_money()+"--"+self.member.monthly_original_price())

        print('打开交易记录')
        self.member.transaction_record().click()
        time.sleep(1)
        print('交易记录第一位 信息：'+self.member.opt1_title()+"--"+self.member.opt1_type()+"--"+self.member.opt1_pay_time()+"--"+self.member.opt1_order_No()+"")

        print('返回续费页')
        self.member.my_member_back().click()



