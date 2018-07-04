#coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

def statistics():
    tmp = {}
    counter = 0
    filelist = [i for i in os.listdir() if re.match(".*\.txt", i)]
    for item in filelist:
        path = os.path.abspath(item)
        file = pd.read_table(path, header=None, index_col=None)
        file = file.values.flatten() #numpyのndarrayにして1次元化
        ave = file.mean()
        sem = file.std(ddof = 1)/((file.size)**(1/2)) #不偏標準偏差にするため
        tmp[counter] = [ave, sem, item.replace(".txt", "")] #
        counter += 1
    return tmp

def bargraph(dic):
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(fname='/library/Fonts/ipagp.ttf', size=14)
    fig = plt.figure("Statistics")
    order = [5,1,4,2,3,0]
    name = ["はじめだけ1/2法","はじめだけランダム", "毎回判断ver.2", "毎回判断ver.1", "1/2法", "ランダム選択"]
    color = ["forestgreen", "limegreen", "blue", "dodgerblue", "red", "white"]
    x = 0
    for i in order:
        plt.barh(x, dic[i][0], xerr = dic[i][1], color = color[x], ecolor="black", capsize=5, linewidth = 1, edgecolor = "#000000")
        x += 1
    plt.yticks(range(6), name, fontproperties=fp)
    plt.xticks(size = 14)
    plt.xlim([0,10])
    ax = plt.subplot(1,1,1)
    ax.set_xlabel("当てるまでにかかった試行回数（回）", fontproperties=fp)
    plt.show()


if __name__ == '__main__':
    bargraph(statistics())