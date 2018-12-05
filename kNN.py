import numpy as np
import operator
def createDataSet():
    #创建一个 四组二维的特征向量
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    #四组特征向量的标签
    labels = ['爱情片','爱情片','动作片','动作片']
    return group,labels
# if __name__ == '__main__':
#     #创建数据集
#     group,labels = createDataSet()
#     #打印数据集
#     print(group)
#     print(labels)


def classify0(inX,dataSet,labels,k):
    #numpy函数shape[0]返回dataSet的行数
    dataSetSize  = dataSet.shape[0]
    #在列向量方向上重复inX共1次，因为只有一列
    #在行向量方向上重复inX共dataSetSize次。因为有多行
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    #二维特征相减后平方
    sqDiffMat = diffMat **2
    #sum()所有元素相加，sum(0)列相加，sum（1）行相加
    sqDistances = sqDiffMat.sum(axis = 1)
    #开方，计算出距离
    distances = sqDistances ** 0.5
    #返回distances中距离从小到大排序后的索引值
    sortedDistIndices = distances.argsort()
    #定一个记录类别次数的字典
    classCount = {}
    for i in range(k):
        #取出前k个元素的类别
        voteIlabel = labels[sortedDistIndices[i]]
        #dict.get(key,default=None),字典中的get()方法，返回指定键的值，如果值不在字典中，返回默认值
        #计算类别的次数
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        '''
        python3中用items()替换了2.7版本中的iteritems（）
        key = operator.itemgetter(1)根据字典的值进行排序
        key = operator.itemgetter(0)根据字典的键进行排序
        reverse降序排序字典        
        '''
        sortedClassCount = sorted(classCount.items(),
                                  key = operator.itemgetter(1),reverse =True)
        #返回次数最多的类别，即所要分类的类别
        return sortedClassCount[0][0]
if __name__ == "__main__":
    #创建数据集
    group,labels = createDataSet()
    #测试集
    test = [101,20]
    #kNN分类
    test_class = classify0(test,group,labels,3)
    #打印分类结果
    print(test_class)