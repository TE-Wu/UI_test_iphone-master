# coding=utf-8
import configparser


def read_my_ini(*args):
    config = configparser.ConfigParser()

    # 要改成自己本地的地址
    config.read('/Users/yana/Downloads/UI_test_iphone-master/config/findment.ini')
    value = config.get(*args)
    return value


class ReadIni(object):
    pass


if __name__ == '__main__':
    read_init = ReadIni()
    # print(read_init.read_my_ini('LoginElement','newlogin'))
