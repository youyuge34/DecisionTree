# encoding: utf-8
"""
@author: yousheng
@contact: 1197993367@qq.com
@site: http://youyuge.cn

@version: 1.0
@license: Apache Licence
@file: trees.py
@time: 17/9/1 下午8:10

"""
from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    """
    计算给定数据集的香农熵
    :param dataSet:
    :return:
    """
    num = len(dataSet)
    labels = {}     #dict存储记录不同类别的个数
    for entry in dataSet:
        label = entry[-1]
        if label not in labels:
            labels[label] = 0
        labels[label] += 1
    shannonEnt = 0.0
    for key,value in labels.items():
        prob = float(value)/num
        shannonEnt += -prob* log(prob,2)
    return shannonEnt
