"""
Process data of pore-pressure
"""
import matplotlib.font_manager as fm
legend_font = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc', size=15)
label_font = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc', size=17)
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['font.family']='sans-serif' #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import numpy as np
import pandas as pd


class Graph:
    @staticmethod
    def read_data(path: str)->list:
        '''
        Read data from file
        :param path:
        :return: A list like obj
        '''
        res = list()
        with open(path, 'r') as f:
            for line in f:
                line = float(line.strip())
                res.append(line)
        return res

    @staticmethod
    def remove_duplicate_merge_pair(x: list, y: list):
        '''
        Remove invalid y point(0) and merge x and y into pair
        :param x: x data
        :param y: y data
        :return: list of tuple
        '''
        res = [(time, pore) for time, pore in zip(x, y) if pore > float(0)]
        X = [item[0] for item in res]
        Y = [item[1] for item in res]
        return X, Y

    @staticmethod
    def even_odd_merge_pair(x: list, y: list):
        """
        For pore pressure versus time ,it acts weirdly:pressure after previous one will move on the contract direction"
        :param x: time step
        :param y: pore pressure
        :return:X, Y
        """
        odd_res = [(time, pressure) for index, (time, pressure) in enumerate(zip(x, y)) if index % 2 == 1]
        odd_X = [item[0] for item in odd_res]
        odd_Y = [item[1] for item in odd_res]
        return odd_X, odd_Y
        # even_res = [(time, pressure) for index, (time, pressure) in enumerate(zip(x, y)) if index % 2 == 0]
        # even_X = [item[0] for item in even_res]
        # even_Y = [item[1] for item in even_res]
        # return odd_X, odd_Y, even_X, even_Y
        # return even_X, even_Y

    @staticmethod
    def dd_merge_pair(x: list, y: list):
        """
        For pore pressure versus time ,it acts weirdly:pressure after previous one will move on the contract direction"
        :param x: time step
        :param y: pore pressure
        :return:X, Y
        """
        odd_res = [(time, pressure) for index, (time, pressure) in enumerate(zip(x, y)) if index % 2 == 1]
        odd_X = [item[0] for item in odd_res]
        odd_Y = [item[1] for item in odd_res]
        return odd_X, odd_Y

    @staticmethod
    def even_merge_pair(x: list, y: list):
        """
        For pore pressure versus time ,it acts weirdly:pressure after previous one will move on the contract direction"
        :param x: time step
        :param y: pore pressure
        :return:X, Y
        """
        even_res = [(time, pressure) for index, (time, pressure) in enumerate(zip(x, y)) if index % 2 == 0]
        even_X = [item[0] for item in even_res]
        even_Y = [item[1] for item in even_res]
        return even_X, even_Y

    @staticmethod
    def plot_data(x, y):
        '''
        Plot the data
        :param x: x axis
        :param y: y axis
        :return: None
        '''
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()

    @staticmethod
    def plot_comparision_open_size(x, y, tabel_title="Comaprision", tabel_legend=["Tabel Legend: Legend"]):
        # plt.style.use("seaborn-whitegrid")
        fig, ax = plt.subplots()
        colors = ['k', 'b', 'r', 'm', 'y', 'g', 'c', 'w']
        markers = ['o',  's', '^', 'v', 'p']
        for index in range(len(x)):
            ax.plot(x[index], y[index], colors[index] + markers[index] +"--", label=tabel_legend[index], markevery=3)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        ax.set_xlabel("时间(s)",  fontproperties=label_font)
        ax.set_ylabel("裂纹张开尺寸(cm)",  fontproperties=label_font)
        # ax.set_title(tabel_title, fontproperties=myfont)
        ax.legend(loc='upper right', shadow=True, prop=legend_font)
        ax.set_xlim(right=120)
        ax.set_ylim(top=0.8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()

    @staticmethod
    def plot_comparision_pore_pressure(x, y, tabel_title="Comaprision", tabel_legend=["Tabel Legend: Legend"]):
        # plt.style.use("seaborn-whitegrid")
        # plt.style.use("ggplot")
        fig, ax = plt.subplots()
        colors = ['k', 'b', 'r', 'm', 'y', 'g', 'c', 'w']
        markers = ['o', 's', '^', 'v', 'p']
        # lines = ['--', '-', ':']
        for index in range(len(x)):
            ax.plot(x[index], y[index], colors[index] + markers[index]+"--", label=tabel_legend[index], markevery=3)
            # ax.plot(x[index], y[index], colors[index] + lines[index], label=tabel_legend[index])
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        ax.set_xlabel("时间(s)", fontproperties=label_font)
        ax.set_ylabel("孔压(Pa)", fontproperties=label_font)
        ax.set_ylim(bottom=0)
        # ax.set_title(tabel_title, fontproperties=myfont)
        # ax.set_title(tabel_title)
        ax.legend(loc='upper right', shadow=True, prop=legend_font)
        ax.set_xlim(right=120)
        ax.set_ylim(top=1000000)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.show()

    @staticmethod
    def plot_coordinates(paths, tabel_legend):
        # plt.style.use("classic")
        fig, ax = plt.subplots()
        colors = ['k', 'b', 'r', 'm', 'y', 'g', 'c', 'w']
        markers = ['o', 's', '^', 'v', 'p']
        for index, path in enumerate(paths):
            df = pd.read_csv(path)
            # x = df.iloc[:, 5]
            # y = df.iloc[:, 6]
            x = df.iloc[:, 2]
            y = df.iloc[:, 3]
            ax.plot(x, y, colors[index]+'--'+markers[index], label=tabel_legend[index])
        ax.set_xlim(left=0, right=12)
        ax.set_ylim(bottom=0, top=13)
        ax.set_xlabel("X(m)")
        ax.set_ylabel("Y(m)")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(loc='upper right', shadow=True, prop=myfont)
        plt.show()


if __name__ == "__main__":
    # X_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_time.csv")
    # Y_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_size.csv")
    # X_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_time_0.csv")
    # Y_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_size_0.csv")
    # X_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_time_1.csv")
    # Y_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_size_1.csv")
    # X_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_time_2.csv")
    # Y_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_size_size_2.csv")
    # X_0, Y_0 = Graph.remove_duplicate_merge_pair(X_0, Y_0)
    # X_1, Y_1 = Graph.remove_duplicate_merge_pair(X_1, Y_1)
    # X_2, Y_2 = Graph.remove_duplicate_merge_pair(X_2, Y_2)
    # X_3, Y_3 = Graph.remove_duplicate_merge_pair(X_3, Y_3)
    # # plot_comparision_open_size([X_0, X_1, X_2, X_3], [Y_0, Y_1, Y_2, Y_3], tabel_title="孔隙率对裂纹开口尺寸的影响", tabel_legend=["孔隙率:1", "孔隙率:0.01", "孔隙率:0.2", "孔隙率: 0.5"])
    # # plot_comparision_open_size([X_1, X_2, X_3], [Y_1, Y_2, Y_3], tabel_title="孔隙率对裂纹开口尺寸的影响", tabel_legend=["孔隙率:0.01", "孔隙率:0.2", "孔隙率: 0.5"])
    # Graph.plot_comparision_open_size([X_1, X_2, X_3], [Y_1, Y_2, Y_3], tabel_title="孔隙率对裂纹开口尺寸的影响", tabel_legend=["孔隙率:0.5", "孔隙率:0.2", "孔隙率: 0.01"])

    # X_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_time.csv")
    # Y_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_pre.csv")
    # X_0, Y_0 = Graph.even_odd_merge_pair(X_0, Y_0)
    # X_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_time_0.csv")
    # Y_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_pre_0.csv")
    # X_1, Y_1 = Graph.even_odd_merge_pair(X_1, Y_1)
    # X_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_time_1.csv")
    # Y_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_pre_1.csv")
    # X_2, Y_2 = Graph.even_odd_merge_pair(X_2, Y_2)
    # X_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_time_2.csv")
    # Y_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\poros\middle_crack_pre_pre_2.csv")
    # X_3, Y_3 = Graph.even_odd_merge_pair(X_3, Y_3)
    # # plot_comparision([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="Effects of permeability on pore pressure", tabel_legend=["Even Permeability:2e-5", "Even Permeability:2e-7", "Even Permeability:2e-9", "Even Permeability:2e-11", "Even Permeability:2e-4"])
    # # plot_comparision_pore_pressure([X_0, X_1, X_2, X_3], [Y_0, Y_1, Y_2, Y_3], tabel_title="孔隙率对孔压的影响", tabel_legend=["孔隙率:1", "孔隙率:0.01", "孔隙率:0.2", "孔隙率:0.5"])
    # Graph.plot_comparision_pore_pressure([X_1, X_2, X_3], [Y_1, Y_2, Y_3], tabel_title="孔隙率对裂纹内孔压的影响", tabel_legend=["孔隙率:0.01", "孔隙率:0.2", "孔隙率:0.5"])

    # X_0 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_time.csv")
    # Y_0 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_pre.csv")
    # X_0, Y_0 =  Graph.even_odd_merge_pair(X_0, Y_0)
    # X_1 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_time_1.csv")
    # Y_1 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_pre_1.csv")
    # X_1, Y_1 = Graph.even_odd_merge_pair(X_1, Y_1)
    # X_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_time_2.csv")
    # Y_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_pre_2.csv")
    # X_2, Y_2 = Graph.even_odd_merge_pair(X_2, Y_2)
    # X_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_time_3.csv")
    # Y_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_pre_3.csv")
    # X_3, Y_3 = Graph.even_odd_merge_pair(X_3, Y_3)
    # X_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_time_4.csv")
    # Y_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_pre_pre_4.csv")
    # X_4, Y_4 = Graph.even_odd_merge_pair(X_4, Y_4)
    # # plot_comparision([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="Effects of permeability on pore pressure", tabel_legend=["Even Permeability:2e-5", "Even Permeability:2e-7", "Even Permeability:2e-9", "Even Permeability:2e-11", "Even Permeability:2e-4"])
    # # plot_comparision_pore_pressure([X_0, X_1, X_4], [Y_0, Y_1, Y_4], tabel_title="Effects of permeability on pore pressure", tabel_legend=["Permeability:2e-5", "Permeability:2e-7", "Permeability:2e-4"])
    # Graph.plot_comparision_pore_pressure([X_4, X_0, X_1], [Y_4, Y_0, Y_1], tabel_title="渗透系数对裂纹内孔压影响", tabel_legend=["渗透系数:2e-4", "渗透系数:2e-5", "渗透系数:2e-7"])

    # X_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_time.csv")
    # Y_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_size.csv")
    # X_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_time_1.csv")
    # Y_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_size_1.csv")
    # X_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_time_2.csv")
    # Y_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_size_2.csv")
    # X_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_time_3.csv")
    # Y_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_size_3.csv")
    # X_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_time_4.csv")
    # Y_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\permeability\middle_crack_size_size_4.csv")
    # X_0, Y_0 = Graph.remove_duplicate_merge_pair(X_0, Y_0)
    # X_1, Y_1 = Graph.remove_duplicate_merge_pair(X_1, Y_1)
    # X_2, Y_2 = Graph.remove_duplicate_merge_pair(X_2, Y_2)
    # X_3, Y_3 = Graph.remove_duplicate_merge_pair(X_3, Y_3)
    # X_4, Y_4 = Graph.remove_duplicate_merge_pair(X_4, Y_4)
    # Graph.plot_comparision_open_size([X_4, X_0, X_1], [Y_4, Y_0, Y_1], tabel_title="渗透系数对裂纹开口尺寸的影响", tabel_legend=["渗透系数:2e-4", "渗透系数:2e-5", "渗透系数:2e-7"])


    # X_0 = read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_time_1.csv")
    # Y_0 = read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_size_1.csv")
    # X_0, Y_0 = remove_duplicate_merge_pair(X_0, Y_0)
    # X_1 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_time_1.csv")
    # Y_1 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_size_1.csv")
    # X_1, Y_1 = remove_duplicate_merge_pair(X_1, Y_1)
    # X_2 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_time_2.csv")
    # Y_2 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_size_2.csv")
    # X_2, Y_2 = remove_duplicate_merge_pair(X_2, Y_2)
    # X_3 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_time_3.csv")
    # Y_3 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_size_3.csv")
    # X_3, Y_3 = remove_duplicate_merge_pair(X_3, Y_3)
    # X_4 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_time_4.csv")
    # Y_4 = read_data(r"D:\论文产出\小论文\py_thesis\data\leakoff\middle_crack_size_size_4.csv")
    # X_4, Y_4 = remove_duplicate_merge_pair(X_4, Y_4)
    # plot_comparision_open_size([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="界面滤失系数对裂纹尺寸的影响", tabel_legend=["滤失系数:e-16", "滤失系数:e-12", "滤失系数:e-14", "滤失系数：e-18", "滤失系数：e-20"])
    # # plot_comparision_open_size([X_0, X_4], [Y_0, Y_4], tabel_title="界面滤失系数对裂纹尺寸的影响", tabel_legend=["滤失系数:e-16", "滤失系数:e-12"])

    X_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_time.csv")
    Y_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_size_size.csv")
    X_0, Y_0 = Graph.remove_duplicate_merge_pair(X_0, Y_0)
    X_1 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_time_1.csv")
    Y_1 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_size_1.csv")
    X_1, Y_1 =  Graph.remove_duplicate_merge_pair(X_1, Y_1)
    X_2 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_time_2.csv")
    Y_2 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_size_2.csv")
    X_2, Y_2 =  Graph.remove_duplicate_merge_pair(X_2, Y_2)
    X_3 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_time_3.csv")
    Y_3 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_size_3.csv")
    X_3, Y_3 =  Graph.remove_duplicate_merge_pair(X_3, Y_3)
    X_4 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_time_4.csv")
    Y_4 =  Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_size_size_4.csv")
    X_4, Y_4 =  Graph.remove_duplicate_merge_pair(X_4, Y_4)
    # plot_comparision_open_size([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="流体粘度对裂纹尺寸的影响", tabel_legend=["流体粘度:e-16", "流体粘度:e-12", "流体粘度:e-14", "流体粘度：e-18", "流体粘度：e-20"])
    Graph.plot_comparision_open_size([X_1, X_0, X_4], [Y_1, Y_0, Y_4], tabel_title="流体粘度对裂纹开口尺寸的影响", tabel_legend=["流体粘度:e-12","流体粘度:e-16",  "流体粘度:e-20"])

    # X_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_time.csv")
    # Y_0 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\base\middle_crack_pre_pre.csv")
    # X_0, Y_0 = Graph.even_odd_merge_pair(X_0, Y_0)
    # X_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_time_1.csv")
    # Y_1 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_pre_1.csv")
    # X_1, Y_1 = Graph.even_odd_merge_pair(X_1, Y_1)
    # X_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_time_2.csv")
    # Y_2 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_pre_2.csv")
    # X_2, Y_2 = Graph.even_odd_merge_pair(X_2, Y_2)
    # X_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_time_3.csv")
    # Y_3 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_pre_3.csv")
    # X_3, Y_3 = Graph.even_odd_merge_pair(X_3, Y_3)
    # X_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_time_4.csv")
    # Y_4 = Graph.read_data(r"D:\论文产出\小论文\py_thesis\data\viscosity\middle_crack_pre_pre_4.csv")
    # X_4, Y_4 = Graph.even_odd_merge_pair(X_4, Y_4)
    # # plot_comparision([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="Effects of permeability on pore pressure", tabel_legend=["Even Permeability:2e-5", "Even Permeability:2e-7", "Even Permeability:2e-9", "Even Permeability:2e-11", "Even Permeability:2e-4"])
    # # plot_comparision_pore_pressure([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="流体粘度对裂纹内孔压的影响", tabel_legend=["流体粘度:e-16", "流体粘度:e-12", "流体粘度:e-14", "流体粘度：e-18", "流体粘度：e-20"])
    # Graph.plot_comparision_pore_pressure([X_1, X_0,  X_4], [Y_1, Y_0,  Y_4], tabel_title="流体粘度对裂纹内孔压的影响", tabel_legend=["流体粘度:e-12", "流体粘度:e-16",   "流体粘度:e-20"])


    # X_0 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2049.csv")
    # Y_0 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2049.csv")
    # X_0, Y_0 = even_odd_merge_pair(X_0, Y_0)
    # X_1 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2051.csv")
    # Y_1 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2051.csv")
    # X_1, Y_1 = even_odd_merge_pair(X_1, Y_1)
    # X_2 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2053.csv")
    # Y_2 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2053.csv")
    # X_2, Y_2 = even_odd_merge_pair(X_2, Y_2)
    # X_3 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2104.csv")
    # Y_3 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2104.csv")
    # X_3, Y_3 = even_odd_merge_pair(X_3, Y_3)
    # X_4 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2112.csv")
    # Y_4 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2112.csv")
    # X_4, Y_4 = even_odd_merge_pair(X_4, Y_4)
    # X_5 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_time_2127.csv")
    # Y_5 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\poros\middle_crack_poros_poros_2127.csv")
    # X_5, Y_5 = even_odd_merge_pair(X_5, Y_5)
    # plot_comparision_pore_pressure([X_0, X_1, X_2, X_3, X_4], [Y_0, Y_1, Y_2, Y_3, Y_4], tabel_title="尺寸对裂纹内孔压的影响", tabel_legend=["excavatoion:15", "excavatoion:17", "excavatoion:19", "excavatoion:21", "excavatoion:23", "excavatoion:13"])

    # X_0 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2049.csv")
    # Y_0 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2049.csv")
    # X_0, Y_0 = remove_duplicate_merge_pair(X_0, Y_0)
    # X_1 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2051.csv")
    # Y_1 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2051.csv")
    # X_1, Y_1 = remove_duplicate_merge_pair(X_1, Y_1)
    # X_2 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2053.csv")
    # Y_2 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2053.csv")
    # X_2, Y_2 = remove_duplicate_merge_pair(X_2, Y_2)
    # X_3 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2104.csv")
    # Y_3 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2104.csv")
    # X_3, Y_3 = remove_duplicate_merge_pair(X_3, Y_3)
    # X_4 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2112.csv")
    # Y_4 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2112.csv")
    # X_4, Y_4 = remove_duplicate_merge_pair(X_4, Y_4)
    # X_5 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_time_2127.csv")
    # Y_5 = read_data(r"D:\thesis\mini-thesis\py_thesis\data\size-effect\open_size\size_size_2127.csv")
    # X_5, Y_5 = remove_duplicate_merge_pair(X_5, Y_5)
    # # plot_comparision_open_size([X_0, X_1, X_2, X_3, X_4, X_5], [Y_0, Y_1, Y_2, Y_3, Y_4, Y_5], tabel_title="开挖尺寸对裂纹尺寸的影响", tabel_legend=["excavatoion:15", "excavatoion:17", "excavatoion:19", "excavatoion：21", "excavatoion：23", "excavatoion：13"])
    # plot_comparision_open_size([X_1, X_2, X_3], [Y_1, Y_2, Y_3], tabel_title="开挖尺寸对裂纹尺寸的影响", tabel_legend=["excavatoion:17", "excavatoion:19", "excavatoion：21"])
    # # plot_comparision_open_size([X_0, X_4], [Y_0, Y_4], tabel_title="界面滤失系数对裂纹尺寸的影响", tabel_legend=["滤失系数:e-16", "滤失系数:e-12"])

    # x = Graph.read_data(r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\x_Centrifuge-2018-12-13-16-49.txt")
    # y = Graph.read_data(r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\y_Centrifuge-2018-12-13-16-49.txt")
    # x_merged, y_merged = Graph.even_merge_pair(x, y)
    # Graph.plot_data(x_merged, y_merged)
    # Graph.plot_data(x, y)
    # path_7 = r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\coordinates\amplitude_1\abaqus_7.csv"
    # path_8 = r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\coordinates\amplitude_1\abaqus_8.csv"
    # path_9 = r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\coordinates\amplitude_1\abaqus_9.csv"
    # path_10 = r"D:\thesis\mini-thesis\py_thesis\data\abqus_script_result\coordinates\amplitude_1\abaqus_10.csv"
    # paths = [path_7, path_8, path_9]
    # annotations = ["开挖：7m", "开挖：8m", "开挖：9m"]
    # Graph.plot_coordinates(paths, annotations)