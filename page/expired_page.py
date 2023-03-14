# coding=utf-8

from base.basepage import FindElement


class Expired_Page:
    """
    过期页
    """

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    def head_img(self):
        return self.find.get_element("Expired_page", "head_img")

    def user_name(self):
        return self.find.get_element("Expired_page", "user_name").text

    def message(self):
        return self.find.get_element("Expired_page", "message").text

    def user_number(self):
        return self.find.get_element("Expired_page", "user_number").text

    # 续费会员
    def renewal_member(self):
        return self.find.get_element("Expired_page", "renewal_member")

    def live_button(self):
        return self.find.get_element("Expired_page", "live_button")

    def coming_online(self):
        return self.find.get_element("Expired_page", "coming_online")

    def my_home_back(self):
        return self.find.get_element("Expired_page", "my_home_back")

    def my_home_username(self):
        return self.find.get_element("Expired_page", "my_home_username").text

    def my_home_userlevel(self):
        return self.find.get_element("Expired_page", "my_home_userlevel").text

    def my_home_out(self):
        return self.find.get_element("Expired_page", "my_home_out")

    def my_home_out_cannel(self):
        return self.find.get_element("Expired_page", "my_home_out_cannel")

    def my_home_out_true(self):
        return self.find.get_element("Expired_page", "my_home_out_true")

    def my_home_endtime(self):
        return self.find.get_element("Expired_page", "my_home_endtime").text

    def coming_online_back(self):
        return self.find.get_element("Expired_page", "coming_online_back")

    def renewal_member_back(self):
        return self.find.get_element("Expired_page", "renewal_member_back")

    def transaction_back(self):
        return self.find.get_element("Expired_page", "transaction_back")

    def transaction_button(self):
        return self.find.get_element("Expired_page", "transaction_button")

    # 交易记录内容1
    def transaction1(self):
        return self.find.get_element("Expired_page", "transaction1")

    def live_back(self):
        return self.find.get_element("Expired_page", "live_back")

    def live_opt1(self):
        return self.find.get_element("Expired_page", "live_opt1")

    def live_opt1_movie_name(self):
        return self.find.get_element("Expired_page", "live_opt1_movie_name")

    def live_opt1_movie_number(self):
        return self.find.get_element("Expired_page", "live_opt1_movie_number")
