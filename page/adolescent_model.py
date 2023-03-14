# -*- coding:utf-8 -*-

from base.basepage import FindElement


class Adolescent_Model:
    """
    模式选择页面
    """

    def __init__(self, driver):
        self.driver = driver
        self.find = FindElement(driver)

    # 选择标准模式
    def standard_button(self):
        return self.find.get_element('Pattern', 'standard')

    # 选择青少年模式
    def teenagers_button(self):
        return self.find.get_element('Pattern', 'teenagers')

    # 个人中心设置-青少年模式
    def adolescent_button(self):
        return self.find.get_element('MyMore', 'adolescent')

    # 开启青少年模式页
    def not_open(self):
        return self.find.get_element('MyMore', 'not_open')

    # 开启青少年模式
    def open_baby_button(self):
        return self.find.get_element('MyMore', 'open_baby')

    # 输入密码
    def set_pwd(self):
        return self.find.get_element('MyMore', 'set1_pwd')

    # 设置密码
    def set_password(self):
        return self.find.get_element('MyMore', 'set_password').text

    # 确认密码
    def confirm_password(self):
        return self.find.get_element('MyMore', 'confirm_password').text

    # 返回
    def adolescent_back(self):
        return self.find.get_element('MyMore', 'adolescent_back')

    # 青少年首页每日推荐影片信息
    def moviename(self):
        return self.find.get_element('Pattern', 'moviename').text

    def movietype(self):
        return self.find.get_element('Pattern', 'movietype').text

    # 青少年首页-退出
    def out_adolescent(self):
        return self.find.get_element('Pattern', 'out_adolescent')

    # 退出青少年模式页
    def out_type(self):
        return self.find.get_element('Pattern', 'outtype')

    # 退出青少年模式
    def out_ado(self):
        return self.find.get_element('Pattern', 'out_ado')

    # 退出青少年密码
    def out_pwd(self):
        return self.find.get_element('Pattern', 'out_pwd')

    # 忘记密码
    def forget_pwd_button(self):
        return self.find.get_element('Pattern', 'forget_pwd')

    # 联系客服-取消
    def cancel_call_button(self):
        return self.find.get_element('Pattern', 'cancel_call')

    # 重置密码
    def reset_pwd_button(self):
        return self.find.get_element('Pattern', 'reset_pwd')

    # 输入原密码提示
    def original_pwd(self):
        return self.find.get_element('Pattern', 'original_pwd')

    # 输入新密码
    def new_pwd(self):
        return self.find.get_element('Pattern', 'new_pwd')

    # 确认新密码
    def again_pwd(self):
        return self.find.get_element('Pattern', 'again_pwd')
