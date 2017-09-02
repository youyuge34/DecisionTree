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


def splitDataSet(dataSet, axis, value):
    """
    按照给定特征划分数据集
    :param dataSet:
    :param axis: 划分数据集的第几个特征
    :param value: 特征==特征值
    :return:
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

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


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 特征值数量
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1
    for i in range(numFeatures):
        tempList = [x[i] for x in dataSet]
        values = set(tempList)  # 第i个特征值可能的取值集合
        newEntropy = 0.0
        for value in values:
            tempMat = splitDataSet(dataSet, i, value)
            prob = float(len(tempMat)) / len(dataSet)  # 权重
            newEntropy += prob * calcShannonEnt(tempMat)  # 若分解第i个属性，值为value时的熵
        infoGain = baseEntropy - newEntropy  # 信息增益(无序度的减少)
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
