#coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

def statistics():
    tmp = {}
    filelist = [i for i in os.listdir() if re.match(".*\.txt", i)]
    for item in filelist:
        path = os.path.abspath(item)
        file = pd.read_table(path, header=None, index_col=None)
        file = file.values.flatten()
        ave = file.mean()
        sem = file.std(ddof = 1)/((file.size)**(1/2))
        tmp[item.replace(".txt", "")] = [ave, sem]
    return tmp

def bargraph(dic):
    fig = plt.figure("Statistics")
    for k, v in dic.items():
        plt.barh(k, v[0], xerr = v[1], ecolor="black", capsize=5, linewidth = 1, edgecolor = "#000000")
    plt.show()


if __name__ == '__main__':
    bargraph(statistics())
