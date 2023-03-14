# coding=utf-8

from base.basepage import FindElement

"""
 影片详情页
"""
class Movie_Detail:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 详情页返回
    def detail_close(self):
        return self.find.get_element('MovieDetails', 'close')

    # 详情页点击片单
    def joincoollect(self):
        return self.find.get_element('MovieDetails', 'joincoollect')

    # 点击播放
    def play(self):
        return self.find.get_element('MovieDetails', 'play')
    #分享
    def share_button(self):
        return self.find.get_element('MovieDetails', 'share')
    #下载
    def download_button(self):
        return self.find.get_element('MovieDetails', 'download')


    # 一拳超人详情页概要
    def yqcrtitle_button(self):
        return self.find.get_element('MovieDetails', 'yqcrdetail')

    # 白鹿原详情页概要
    def blytitle_button(self):
        return self.find.get_element('MovieDetails', 'blydetail')

    # 斯巴达克斯详情页概要
    def sbdkstitle_button(self):
        return self.find.get_element('MovieDetails', 'sbdksdetail')

    # 详情页 x 键
    def close_button(self):
        return self.find.get_element('MovieDetails', 'close')

    # 详情页 评价 键
    def evaluate_button(self):
        return self.find.get_element('MovieDetails', 'evaluate')
    #点赞喜欢
    def praisse_button(self):
        return self.find.get_element('MovieDetails', 'praisse')
    #点赞不喜欢
    def taead_button(self):
        return self.find.get_element('MovieDetails', 'taead')
    #大关闭
    def bigclose_button(self):
        return self.find.get_element('MovieDetails', 'bigclose')
    #评价完了 喜欢
    def like_button(self):
        return self.find.get_element('MovieDetails', 'like')
    #不喜欢
    def nolike_button(self):
        return self.find.get_element('MovieDetails', 'nolike')


    # 点击下载
    def download(self):
        return self.find.get_element('MovieDetails', 'download')

# 下载浮层
    # 高清按钮
    def high(self):
        return self.find.get_element('MovieDetails', 'high')

    # 标清按钮
    def standard(self):
        return self.find.get_element('MovieDetails', 'standard')

    # 剧集列表第一集
    def first_down(self):
        return self.find.get_element('MovieDetails', 'first_down')

    # 关闭浮层
    def down_close(self):
        return self.find.get_element('MovieDetails', 'down_close')

    # 查看我的缓存
    def my_down(self):
        return self.find.get_element('MovieDetails', 'my_down')

# 影评
    # 影评按钮
    def review_button(self):
        return self.find.get_element('MovieDetails', 'review_button')

    # 影评内容
    def review_text(self):
        return self.find.get_element('MovieDetails', 'review_text')

    # 影评列表头像
    def review_img(self):
        return self.find.get_element('MovieDetails', 'review_img')

    # 影评x
    def review_x(self):
        return self.find.get_element('MovieDetails', 'review_x')

    # 影评列表点赞
    def review_fabulous(self):
        return self.find.get_element('MovieDetails', 'review_fabulous')

    # 影评编辑按钮
    def review_edit(self):
        return self.find.get_element('MovieDetails', 'review_edit')

    # 屏蔽此人
    def option1(self):
        return self.find.get_element('MovieDetails', 'option1')

    # 涉及政治相关
    def option3(self):
        return self.find.get_element('MovieDetails', 'option3')

    # 二级选项
    def confirm(self):
        return self.find.get_element('MovieDetails', 'confirm')

    def cancel(self):
        return self.find.get_element('MovieDetails', 'cancel')





