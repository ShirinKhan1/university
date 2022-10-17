import time
import subprocess
import re


def readCfg():
    with open('Cfg', 'r') as f:
        for line in f:
            needed_t = 0
            fin_t = 0
            for i in line.split():
                path = r'explorer /select,'
                if i.isdigit():
                    needed_t = int(i)
                elif re.match(r'^-?\d+(?:\.\d+)$', i) is None:
                    path = path + str(i).replace('/', '\\')
                    open_t = time.perf_counter()
                    subprocess.Popen(path)
                    close_t = time.perf_counter()
                    fin_t = close_t - open_t
                    print(fin_t)
            if fin_t <= needed_t:
                print('Success!')
            else:
                print("Fail!")


if __name__ == "__main__":
    readCfg()