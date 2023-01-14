cd  /Users/apple/PycharmProjects/zhongshujiaoben/Test_case/Test_APIcase/
pytest -sq /Users/apple/PycharmProjects/zhongshujiaoben/Test_case/Test_APIcase/test_xiaoxixietong.py --alluredir=/Users/apple/PycharmProjects/zhongshujiaoben/test_report/tmp  -clean-alluredir
allure generate /Users/apple/PycharmProjects/zhongshujiaoben/test_report/tmp -o /Users/apple/PycharmProjects/zhongshujiaoben/test_report/report --clean

