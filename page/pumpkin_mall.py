# coding=utf-8

from base.basepage import FindElement


class Pumpkin_mall:
    """
    南瓜商城
    """

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    def back(self):
        return self.find.get_element("Pumpkin_mall", "back")

    # 选项1的名称
    def opt1_title(self):
        return self.find.get_element("Pumpkin_mall", "opt1_title")

    # 选项1 总计多少
    def opt1_num(self):
        return self.find.get_element("Pumpkin_mall", "opt1_num").text

    # 还差多少
    def opt1_still_bad(self):
        return self.find.get_element("Pumpkin_mall", "opt1_still_bad").text

    # 继续攒
    def keep_saving(self):
        return self.find.get_element("Pumpkin_mall", "keep_saving")

    # 获取南瓜籽 页面
    def pumpkin_seed1(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed1")

    def pumpkin_seed2(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed1.1")

    def pumpkin_seed3(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed3")

    def pumpkin_seed4(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed4")

    def pumpkin_seed5(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed5")

    # 去观影
    def go_movie(self):
        return self.find.get_element("Pumpkin_mall", "go_movie")

    def my_tab(self):
        return self.find.get_element("Pumpkin_mall", "my_tab")

    def user_name(self):
        return self.find.get_element("Pumpkin_mall", "user_name").text

    def user_level(self):
        return self.find.get_element("Pumpkin_mall", "user_level").text

    def user_end_time(self):
        return self.find.get_element("Pumpkin_mall", "user_end_time").text

    def user_pumpkin(self):
        return self.find.get_element("Pumpkin_mall", "user_pumpkin").text

    def get_pumpkin_seed_rules(self):
        return self.find.get_element("Pumpkin_mall", "get_pumpkin_seed_rules")

    def pumpkin_seed_rules(self):
        return self.find.get_element("Pumpkin_mall", "pumpkin_seed_rules")

