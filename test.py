# encoding: utf-8

import trees
import treePlotter

def run():
    dataSet,labels = trees.createDataSet()
    # print dataSet
    # print trees.calcShannonEnt(dataSet)
    # print trees.chooseBestFeatureToSplit(dataSet)
    # print trees.createTree(dataSet, labels)
    myTree = treePlotter.retrieveTree(0)
    # treePlotter.createPlot(myTree)
    # print trees.classify(myTree, labels, [1, 1])
    # trees.storeTree(myTree,'dump.txt')
    # print trees.grabTree('dump.txt')


def testLenses():
    """
    测试隐形眼镜案例
    :return:
    """
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    print lenses
    lensesTree = trees.createTree(lenses, lensesLabels)
    print lensesTree
    treePlotter.createPlot(lensesTree)


if __name__ == '__main__':
    run()
    testLenses()
