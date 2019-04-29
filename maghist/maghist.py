import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_2 = "2um"
path_3 = "3um"
path_m = "mix"

def xlsx_path(path_kind,sheet_num):
    path = "./" + path_kind + "_PIV_10f/10f/" + str(sheet_num) + "/" + path_kind + "_" + str(sheet_num) +"_10f.xlsx"
    return path

def fig_path(path_kind,sheet_num):
    path = "./" + path_kind + "_PIV_10f/10f/" + str(sheet_num) + "/"
    return path

sheet_num = 0
kind = [path_2,path_3,path_m]
number = [0,10,20,50,100,200]
mag_num =[4,9,14]
for path_kind in kind:
    for sheet_num in number:
        for mag in mag_num:
            try:
                xlsx_data = pd.read_excel(xlsx_path(path_kind,sheet_num),usecols = [mag])
            except:
                continue
            xlsx_data = xlsx_data.values
            #xlsx_data = xlsx_data.dropna()
            #xlsx_data = xlsx_data.drop([8111,8112,8113])
            #xlsx_data = np.delete(xlsx_data,)
            xlsx_hist = xlsx_data[0:-3]
            #xlsx_series = xlsx_data.iloc[:,0]

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.hist(xlsx_hist,bins=500)
            ax.set_title('mag_hist_'+ path_kind + str(sheet_num))
            ax = plt.xlabel(path_kind + "magnitude" + str(sheet_num))
            ax = plt.ylabel("number")
            ax = plt.xlim(0,10)
            ax = plt.ylim(0,600)
            fig.savefig(fig_path(path_kind,sheet_num) + 'magcol(' + str(mag) + ')_hist.png')