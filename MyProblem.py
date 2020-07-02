# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea
"""
    定义具体待优化的模型及其对应的约束条件
"""


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self, sampleNum):  # 传入种群数目/规模
        self.net = MyNetwork(sampleNum)  # 交通网络信息类

        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = self.net.varNum  # 初始化Dim（决策变量维数/变量个数）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）

        # 下面四个变量是针对此交通网络设计的定值
        lb = [0]*Dim  # 决策变量下界
        ub = [8]*Dim  # 决策变量上界
        lbin = [1]*Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1]*Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）

        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):  # 目标函数
        Vars = pop.Phen  # 得到决策变量矩阵
        # x1 = Vars[:, [0]]
        # x2 = Vars[:, [1]]  # <class 'numpy.ndarray'>
        # pop.ObjV = x1**2 + 3*x1 + x2**3 - x2 + 7  # 计算目标函数值，赋值给pop种群对象的ObjV属性
        # 采用可行性法则处理约束(注释掉则无约束)
        # pop.CV = np.hstack([x1 + x2 - 5,
        #                 - 2*x1 + x2 + 1])

        # 目标函数的两个部分分别计算，再相加（应该是两个ndarray相加）
        pop.ObjV = self.net.get_obj_part1(Vars) + self.net.get_obj_part2(Vars)

    def calReferObjV(self):  # 设定目标数参考值（本问题目标函数参考值设定为理论最优值）
        referenceObjV = np.array([[2.5]])
        return referenceObjV


from model import TrafficFlowModel
'''
个人定义的网络类，用来调用实现用户均衡的package
'''
class MyNetwork:
    def __init__(self, sampleNum):
        self.sampleNum = sampleNum  # 配合遗传算法使用的种群数量

        # 定义一些交通网络设计时需要的变量
        self.varNum = 5  # 路段数目
        self.Ca = [45, 40, 70, 40, 45]  # 路段的原有通行能力
        self.T0 = [4, 6, 2, 5, 3]  # 路段的零流阻抗
        self.Da = [2.0, 2.0, 1.5, 2.0, 2.0]  # 路段的单位投资成本

        # Graph represented by directed dictionary
        # In order: first ("5", "7"), second ("5", "9"), third ("6", "7")...
        self.graph = [
            ("1", ["2", "3"]),
            ("2", ["3", "4"]),
            ("3", ["4"]),
            ("4", [])
        ]

        # Origin-destination pairs
        self.origins = ["1"]
        self.destinations = ["4"]

        # Demand between each OD pair (Conjugated to the Cartesian
        # product of Origins and destinations with order)
        # self.demand = [65]
        self.demand = [130]
        # self.demand = [180]

    def __bpm(self, t0, xa, ca):
        return t0*(1+0.15*(xa/ca)**4)

    # 计算目标函数的第一部分（路段阻抗成本）
    def get_obj_part1(self, Vars):
        # Ya = {}  # 新增交通量的集合
        # for i in range(self.varNum):
        #     Ya[i] = Vars[:, [i]]
        Xa = self.__get_xa(Vars)  # 各路段分配通行能力的集合
        Ta = 0  # 总的路段阻抗成本（是个ndarray）
        for i in range(self.varNum):
            # 当前通行能力 = 原有通行能力ca + 新增的通行能力ya
            Ta += (self.__bpm(self.T0[i], Xa[:, [i]], self.Ca[i]+Vars[:, [i]]) * Xa[:, [i]])
        return Ta

    # 计算目标函数的第二部分（总投资成本）
    def get_obj_part2(self, Vars):
        Ia = 0  # 总投资成本（是个ndarray）
        for i in range(self.varNum):
            Ia += (self.Da[i] * (Vars[:, [i]]**2))
        return 1.6*Ia

    # 下层规划模型求解：用户均衡 F-W算法
    def __get_xa(self, Vars):
        # todo 调用F-W算法求xa
        Xa = None
        for i in range(self.sampleNum):
            # Initialize the model by data
            mod = TrafficFlowModel(self.graph, self.origins, self.destinations,
                                   self.demand, self.T0, self.__get_cur_Ca(Vars[i, :]))

            # Change the accuracy of solution if necessary
            mod._conv_accuracy = 1e-3
            mod.set_disp_precision(3)

            # Solve the model by Frank-Wolfe Algorithm
            mod.solve()

            # Generate report to console（此处不建议启用）
            # mod.report()

            # Return the solution if necessary
            flow, link_t, path_t, v_c = mod._formatted_solution()
            if i == 0:
                Xa = flow
            else:
                Xa = np.vstack([Xa, flow])
        return Xa
    # Xa应该是一个矩阵，97行中使用的Xa[i]应该是Xa中的第i列

    # 获得当前的通行能力
    def __get_cur_Ca(self, xa):
        cur_ca = xa+self.Ca
        return cur_ca.tolist()

