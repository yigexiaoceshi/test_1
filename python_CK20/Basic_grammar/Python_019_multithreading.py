#!/usr/bin/python3
# -*- coding:utf-8 -*-
import threading
import time


# def apple_1():
#     print("苹果1")
#     time.sleep(1)
# def apple_2():
#     print("苹果2")
#     time.sleep(1)
# def main():
#     start_time = time.time()
#     thread1 = threading.Thread(target=apple_1)
#     thread2 = threading.Thread(target=apple_2)
#     thread1.start()
#     thread2.start()
#     end_time = time.time()
#     print("2个线程一共执行的时长为：",end_time - start_time)
#     print("苹果3")
#     print("有多少个小丑？",threading.active_count())
#     print("这些小丑是谁呢？",threading.enumerate())
# if __name__ == "__main__":
#     main()

# GIL
# 同一时刻，只能有一个线程在运行
def task():
    time.sleep(2)
    print("强制等待2秒")


def main():
    start_time = time.time()
    # #写法1：会执行task方法里的sleep，然后再执行下一个线程
    # thread1 = threading.Thread(target=task())
    # #写法2：2个线程前后脚依次执行，不会等到前一个线程执行完了再开始下一个线程
    # thread1 = threading.Thread(target=task)
    # #写法3：会执行task方法里的语句，完成之后再执行，和写法1类似
    thread1 = threading.Thread(target=task)
    # 写法4：
    # thread1 = threading.Thread(task)  #写法报错
    thread1.start()
    # thread1.join()  # 如果join()方法放在这里，则thread1也会执行方法task()里的语句，再执行下一个线程
    thread2 = threading.Thread(target=task)  # 边执行线程（包含走进task方法）边往下走，同时进行
    thread2.start()
    thread1.join()  # 加入这行代码，意思是当前线程执行完成之前，不会执行下个线程，使得task方法里的sleep生效
    thread2.join()  # 同上
    end_time = time.time()
    print(end_time - start_time)


if __name__ == "__main__":
    main()

# 讲完一脸懵逼，完全没看懂的一个视频，自己上网搜索多线程吧
