# encoding: utf-8

import trees
import treePlotter

def run():
    dataSet,labels = trees.createDataSet()
    # print dataSet
    # print trees.calcShannonEnt(dataSet)
    # print trees.chooseBestFeatureToSplit(dataSet)
    # print trees.createTree(dataSet, labels)
    myTree = treePlotter.retrieveTree(1)
    treePlotter.createPlot(myTree)

if __name__ == '__main__':
    run()