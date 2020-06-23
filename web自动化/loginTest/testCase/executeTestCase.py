import os
import unittest

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    fileName = 'report.html'
    test_dir = os.path.dirname(__file__)
    file_Path = os.path.dirname(os.path.dirname(__file__)) + "/result/report/" + fileName
    print(file_Path)
    discover = unittest.defaultTestLoader.discover(test_dir, '*test.py')
    with open(file_Path, 'wb') as f:
        HTMLTestRunner(stream=f, title='测试报告').run(discover)

