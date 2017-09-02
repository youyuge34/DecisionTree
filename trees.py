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
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # change to discrete values
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
    labels = {}  # dict存储记录不同类别的个数
    for entry in dataSet:
        label = entry[-1]
        if label not in labels:
            labels[label] = 0
        labels[label] += 1
    shannonEnt = 0.0
    for key, value in labels.items():
        prob = float(value) / num
        shannonEnt += -prob * log(prob, 2)
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


def majorityCnt(classList):
    """
    多数表决法，返回一个list中出现最多次的元素名称
    :param classList:
    :return:
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """
    递归创建决策树
    :param dataSet:
    :param labels:
    :return:
    """
    classList = [x[-1] for x in dataSet]
    if len(set(classList)) == 1:
        return classList[0]  # 类别相同则停止继续划分
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)  # 没特征了，但是类别不唯一，用多数表决法
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 最佳分类特征的序号数
    bestLabel = labels[bestFeat]  # 分类特征的名字
    myTree = {bestLabel: {}}

    del (labels[bestFeat])
    featValues = [x[bestFeat] for x in dataSet]
    uniqueValues = set(featValues)  # 该特征的所有值，每个值都生成一个子树
    for value in uniqueValues:
        tempLabels = labels[:]
        myTree[bestLabel][value] = createTree(splitDataSet \
                                                  (dataSet, bestFeat, value), tempLabels)
    return myTree


def classify(inputTree, featLabels, testVec):
    """
    使用决策树的分类函数
    :param inputTree:
    :param featLabels:
    :param testVec:
    :return:
    """
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)  # 将第一个节点名称转换成了对应的index值
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
