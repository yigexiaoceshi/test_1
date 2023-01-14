# debug：最细微的信息记录到debug中，这个级别就是用来debug的，看程序在哪一次迭代中发生了错误，比如每次循环都输出一些东西用debug级别
# info：级别用于routines，也就是输出start finish 状态改变等信息
# warn：输出一些相对重要，但是不是程序bug的信息，比如输入了错误的密码，或者连接较慢
# error：输出程序bug，打印异常信息
# critical：用于处理一些非常糟糕的事情，比如内存溢出、磁盘已满，这个一般较少使用


import logging
import datetime


def logger_config(log_path):

    # 配置log
    # :param log_path: 输出log路径
    # :param logging_name: 记录中name，可随意
    # :return:

    # logger是日志对象，handler是流处理器，console是控制台输出（没有console也可以，将不会在控制台输出，会在日志文件中输出）

    # 获取logger对象,取名
    logger = logging.getLogger()
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    logger.setLevel(level=logging.DEBUG)
    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    # 生成并设置文件日志格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s-%(funcName)s[line:%(lineno)d] - %(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    # console相当于控制台输出，handler文件输出。获取流句柄并设置日志级别，第二层过滤
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 为logger对象添加句柄
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger


# if __name__ == "__main__":
#     logger = logger_config(log_path=f'/Users/apple/PycharmProjects/zhongshujiaoben/LogTools/{datetime.datetime.now().strftime("%Y-%m-%d  %H-%M-%S")}.txt')
#     logger.info("info")
#     logger.error("error")
#     logger.debug("debug")

