import time
import os


def exex_2():
    list_elemts = []
    f = open('cfg2', "r")
    for elem in f:
        list_elemts = elem.split(sep=" ")

    def goto(l):
        while l:
            os.startfile(str(l.pop(0)))
            time.sleep(5)
            goto(l)
    while True:
        if os.path.isfile("ex_2\\cpuz.exe"):
            os.chdir("ex_2")
            goto(list_elemts)
            return False
        print('empty')
        time.sleep(4)


if __name__ == '__main__':
    exex_2()
