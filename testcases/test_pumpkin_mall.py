import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.finmreview_detail import Finmreview_Detail
from page.fristhome import HomePage
from page.movie_detail import Movie_Detail
from page.my_coollect import My_Coollect
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.pumpkin_mall import Pumpkin_mall
from page.video import Video


class Test_Pumpkin_Mall(unittest.TestCase):
    """
    南瓜商城
    """

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.home = HomePage(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mycoollect = My_Coollect(ios_driver)
        self.detail = Movie_Detail(ios_driver)
        self.mall = Pumpkin_mall(ios_driver)

    def test_1(self):

        time.sleep(4)
        print('首页进入个人页')
        self.home.my_home().click()

        print('进入南瓜商城')
        self.myhome.store().click()
        time.sleep(3)
        print('第一位的title：'+self.mall.opt1_title().text)
        print("南瓜籽："+self.mall.opt1_num())

        try:
            self.mall.keep_saving()
            print('南瓜籽不足时展示还差南瓜籽：' + self.mall.opt1_still_bad())

        except Exception:
            print('南瓜籽充足逻辑')
            '''
            因为现在只能购买 会员卡，购买一次后 一段时间内无法再次购买，频繁执行要先充值很多南瓜籽 用到很多账号，所以这段购买逻辑 暂不执行
            '''

            # print('南瓜籽充足 点击立即购买')
            # print('点击立即购买')
            # print('确认订单页')
            # print('用户信息：'+"南瓜籽数：")
            # print('预计消耗南瓜籽数：')
            # print('点击兑换按钮')
            # print('二次选择 选择取消')
            # print('二次选择 选择确认')
            # print('剩余南瓜籽数：')
            # print('返回 回到商店页')

        print('切换到我的tab')
        self.mall.my_tab().click()

        print('个人信息展示：'+self.mall.user_name()+"--"+self.mall.user_pumpkin()+"--"+self.mall.user_level()+"--"+self.mall.user_end_time())

        """
        目前商城内只有会员卡，收货地址目前没用 暂不校验
        """
        # print('判断是否有地址')
        #
        # print('没有地址填写地址')
        #
        # print('有地址：')
        #
        # print('切换地址')
        #
        # print('切换后的地址：')