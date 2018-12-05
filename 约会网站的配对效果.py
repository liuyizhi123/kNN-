import numpy as np
import matplotlib.pyplot as plt
import operator


#使用k-近邻算法改进约会网站的配对效果
def file2matrix(filename):
    #打开文件
    fr = open(filename)
    #读取文件所有内容
    arrayOLines = fr.readlines()
    # 得到文件的行数
    numberOfLines = len(arrayOLines)
    #返回的numpy矩阵，解析完成的数据：numberOfLines行，3列
    returnMat = np.zeros((numberOfLines,3))
    #返回的分类标签向量
    classLabelVector = []
    #行的索引值
    index = 0
    for line in arrayOLines:
        #s.strip(rm)，当rm为空时，默认删除空白符包括（\n \r \t ）
        line = line.strip()
        #使用s.split(str = '',num = string,cout(str))将字符串根据"\t"分隔符进行切片
        listFromLine = line.split('\t')
        #将数据前三列提取出来，存放到returnMat的numpy矩阵中，也就是特征矩阵
        returnMat[index,:] = listFromLine[0:3]
        #根据文本中标记的喜欢程度进行分类，1代表不喜欢，2代表魅力一般，3代表极具魅力
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat,classLabelVector

if __name__ == "__main__":
    #打开的文件名
    filename = "datingTestSet.txt"
    #打开并处理数据
    datingDataMat,datingLabels = file2matrix(filename)
    print(datingDataMat)
    print(datingLabels)

    #数据可视化
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
               15.0* np.array(datingLabels),15.0*np.array(datingLabels))
    plt.show()



