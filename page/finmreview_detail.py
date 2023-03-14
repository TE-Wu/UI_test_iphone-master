# coding=utf-8

from base.basepage import FindElement

"""
影评详情页
"""


class Finmreview_Detail:
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 影评详情

    def fd_input(self):
        return self.find.get_element('Fimreview_Detail', 'input')

    def fd_back(self):
        return self.find.get_element('Fimreview_Detail', 'back')

    def fd_comment(self):
        return self.find.get_element('Fimreview_Detail', 'comment')

    def share(self):
        return self.find.get_element('Fimreview_Detail', 'share')

    def pyp(self):
        return self.find.get_element('Fimreview_Detail', 'pyp')

    def wx(self):
        return self.find.get_element('Fimreview_Detail', 'wx')

    def wb(self):
        return self.find.get_element('Fimreview_Detail', 'wb')

    def like(self):
        return self.find.get_element('Fimreview_Detail', 'like')

    def cannel(self):
        return self.find.get_element('Fimreview_Detail', 'cannel')

    def close(self):
        return self.find.get_element('Fimreview_Detail', 'close')

