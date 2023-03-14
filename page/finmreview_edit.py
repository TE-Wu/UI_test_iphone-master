# coding=utf-8

from base.basepage import FindElement

"""
影评编辑页
"""


class Finmreview_Edit:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 取消
    def cancel(self):
        return self.find.get_element('Fimreview_Edit', 'cancel')

    # 发布
    def push(self):
        return self.find.get_element('Fimreview_Edit', 'push')

    # 输入
    def input(self):
        return self.find.get_element('Fimreview_Edit', 'input')

    # 字体
    def font(self):
        return self.find.get_element('Fimreview_Edit', 'font')

    def font1(self):
        return self.find.get_element('Fimreview_Edit', 'font1')

    def font2(self):
        return self.find.get_element('Fimreview_Edit', 'font2')

    # 添加照片
    def add_img(self):
        return self.find.get_element('Fimreview_Edit', 'add_img')

    # 相册
    def album(self):
        return self.find.get_element('Fimreview_Edit', 'album')

    # 选择相册照片
    def album_img(self):
        return self.find.get_element('Fimreview_Edit', 'album_img')

    # 选择相册完成
    def album_finish(self):
        return self.find.get_element('Fimreview_Edit', 'album_finish')

    # 删除招照片
    def album_x(self):
        return self.find.get_element('Fimreview_Edit', 'album_x')

