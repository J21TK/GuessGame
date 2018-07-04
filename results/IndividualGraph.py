#coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import random
from matplotlib import colors as mcolors

#names_colors.pyより抜粋、ランダムに色を選べる
def colorful():
    sorted_names = list(mcolors.BASE_COLORS)
    return random.choice(sorted_names)

def showgraph():
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(fname='/library/Fonts/ipagp.ttf', size=12)
    
    filelist = [i for i in os.listdir() if re.match(".*\.txt", i)]
    for item in filelist:
        path = os.path.abspath(item)
        file = pd.read_table(path, header=None, index_col=None)
        file = file.T #行列入れ替え
        fig = plt.figure(item.replace(".txt", ""))
        """
        #箱ひげ図を書くには以下を用いる
        ax = fig.add_subplot(111)
        box_plot = ax.boxplot([list(file[i]) for i in file])
        ax.set_xticklabels([i+1 for i in range(len(file))])
        """
        color_ten = ["white", "darkslategrey", "peachpuff", "mediumblue", "yellow", "forestgreen", "aqua", "gold", "darkgray", "crimson"]
        for i in file:
            #if i % 10 == 0:
            #    color = colorful()
            color = color_ten[i//10]
            x = i+1
            y = file[i].mean()
            y_error = file[i].std()/(len(file[i])**(1/2)) #SEM
            plt.errorbar(x, y, yerr = y_error, linestyle = "", linewidth = 0.5, marker = "o", markersize = 4.0, markerfacecolor = color, markeredgecolor = "black", markeredgewidth = 0.5)
        ax = plt.subplot(1,1,1)
        ax.set_xlabel("謎の数の答え", fontproperties=fp)
        ax.set_ylabel("当てるまでにかかった試行回数（回）", fontproperties=fp)
        plt.xticks(size = 12)
        plt.xticks(size = 12)
        plt.ylim(0,12)
    plt.show()

if __name__ == '__main__':
    showgraph()
