# encoding: utf-8

import trees

def run():
    dataSet,labels = trees.createDataSet()
    print dataSet
    print trees.calcShannonEnt(dataSet)
    print trees.chooseBestFeatureToSplit(dataSet)


if __name__ == '__main__':
    run()