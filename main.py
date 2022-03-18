# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea  # import geatpy
from MyProblem import MyProblem  # 导入自定义问题接口

# Set the precision of display, which influences
# only the digit of numerical component in arrays
np.set_printoptions(precision=4)

if __name__ == '__main__':
    """================================实例化问题对象==========================="""
    NIND = 50            # 种群规模
    problem = MyProblem(NIND)  # 生成问题对象
    """==================================种群设置==============================="""
    Encoding = 'RI'       # 编码方式
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)  # 创建区域描述器
    population = ea.Population(Encoding, Field, NIND)  # 实例化种群对象（此时种群还没被初始化，仅仅是完成种群对象的实例化）
    """================================算法参数设置============================="""
    myAlgorithm = ea.soea_DE_rand_1_bin_templet(problem, population)  # 实例化一个算法模板对象
    myAlgorithm.MAXGEN = 50  # 最大进化代数
    myAlgorithm.mutOper.F = 0.5  # 差分进化中的参数F
    myAlgorithm.recOper.XOVR = 0.7  # 重组概率
    myAlgorithm.showCurGen = True  # 显示当前进化代数
    """===========================调用算法模板进行种群进化======================="""
    
    res = ea.optimize(myAlgorithm, verbose=True, drawing=1, outputMsg=True, drawLog=False, saveFlag=True)
    print(res)

    # 输出最后一次的交通流分配信息
    problem.report()

