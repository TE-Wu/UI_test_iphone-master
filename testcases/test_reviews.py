import unittest
import time
from appium import webdriver
from config.wddriver import desired_caps
from page.finmreview_detail import Finmreview_Detail
from page.finmreview_edit import Finmreview_Edit
from page.movie_detail import Movie_Detail
from page.my_home import My_Home
from page.my_movie import My_Movie
from page.seek import Seek
from page.fristhome import HomePage
from page.tobing import ToBing


class Test_Reviews(unittest.TestCase):

    def setUp(self):
        ios_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.home = HomePage(ios_driver)
        self.fd = Finmreview_Detail(ios_driver)
        self.myhome = My_Home(ios_driver)
        self.mvdetail = Movie_Detail(ios_driver)
        self.fe = Finmreview_Edit(ios_driver)

    def test_1(self):
        """
        影评
        """

        print('点击每日推荐详情 进入详情页')
        self.home.details_button().click()

        print('详情页点击我的影评')
        self.mvdetail.review_button().click()

        print('点击编写按钮')
        self.mvdetail.review_edit().click()

        print('影评编辑页写影评')

        print('输入 空格/字符/字母/数字/汉字')
        self.fe.input().send_keys('这部电影都有，小南瓜可以呀！1 整体来讲很好看，推荐 推荐～')

        print('影评添加图片')
        self.fe.add_img().click()

        print('相册页 选择相册')
        self.fe.album().click()

        print('相册页 选择图片')
        self.fe.album_img().click()

        print('相册页 完成')
        self.fe.album_finish().click()

        print('影评编辑页文字颜色')
        self.fe.font1().click()
        self.fe.font2().click()
        self.fe.font().click()

        print('发布影评')
        self.fe.push().click()

        print('影评页面 点击x 选择屏蔽影评')
        self.mvdetail.review_x().ckick()
        self.mvdetail.option1().click()
        self.mvdetail.confirm().click()

        print('影评页举报影评')
        self.mvdetail.review_x().ckick()
        self.mvdetail.option3().click()
        self.mvdetail.confirm().click()

        print('进入影评详情页')
        self.mvdetail.review_text().click()

        print('影评详情页 点击分享')
        self.fd.share().click()

        print('分享到朋友圈')
        self.fd.pyp().click()
        self.fd.cannel().click()

        print('分享到微信')
        self.fd.wx().click()
        self.fd.close().click()

        print('收藏')
        self.fd.like().click()
        self.fd.cannel().click()

        print('回到影片 详情页')
        self.fd.fd_back().click()

        print('影评页 点击头像进入个人信息页')
        self.mvdetail.review_img().click()