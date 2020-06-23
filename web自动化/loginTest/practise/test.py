import time


def foo(param1, *param2):
    print(param1)
    print(param2)

def foo2(bar, lee):
    print(bar, lee)
    print("%s页面中未能找到%s 元素" % ("self", "loc"))

    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
    filePath = "/result/img/" + currentTime + "_" + "login.png"
    filePath = "/result/img/" + currentTime + filePath
    print(filePath)


if __name__ == '__main__':
      foo(1, 2)
      a = [1,2]
      foo2(*a)
