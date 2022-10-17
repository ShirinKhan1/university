import time
import os


def exex_2():

    f = open('cfg2', "r")
    for elem in f:
        list_elements = elem.split(sep=" ")

        def goto(l):
            if not (os.path.isfile(f"ex_2\\{list_elements[0]}")):
                print('empty')
                time.sleep(1)
                goto(l)

        goto(list_elements)
        while list_elements:
                # os.startfile(str(l.pop(0)))
                print(str(list_elements.pop(0)), end=" ")
                time.sleep(1)
        print("\nend")


if __name__ == '__main__':
    exex_2()
