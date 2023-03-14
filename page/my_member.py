# coding=utf-8

from base.basepage import FindElement


class My_Member:
    """
    我的会员
    """
    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    def my_member_back(self):
        return self.find.get_element("My_member", "my_member_back")

    def transaction_record(self):
        return self.find.get_element("My_member", "transaction_record")

    def username(self):
        return self.find.get_element("My_member", "username").text

    def member_end_time(self):
        return self.find.get_element("My_member", "member_end_time").text

    def exclusive_member_tab(self):
        return self.find.get_element("My_member", "exclusive_member_tab").text

    def activate_now_button(self):
        return self.find.get_element("My_member", "activate_now_button")

    def ordinary_member_tab(self):
        return self.find.get_element("My_member", "ordinary_member_tab")

    def member_continuous(self):
        return self.find.get_element("My_member", "member_continuous").text

    def member_money(self):
        return self.find.get_element("My_member", "member_money").text

    def member_ordinary(self):
        return self.find.get_element("My_member", "member_ordinary").text

    def Member_monthly_money(self):
        return self.find.get_element("My_member", "Member_monthly_money").text

    def monthly_original_price(self):
        return self.find.get_element("My_member", "monthly_original_price").text

    def member_season_card(self):
        return self.find.get_element("My_member", "member_season_card").text

    def season_card_money(self):
        return self.find.get_element("My_member", "season_card_money").text

    def season_card_original_price(self):
        return self.find.get_element("My_member", "season_card_original_price").text

    # 交易记录
    def opt1_title(self):
        return self.find.get_element("My_member", "opt1_title").text

    def opt1_type(self):
        return self.find.get_element("My_member", "opt1_type").text

    def opt1_pay_time(self):
        return self.find.get_element("My_member", "opt1_pay_time").text

    def opt1_order_No(self):
        return self.find.get_element("My_member", "opt1_order_No").text

