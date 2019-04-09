import os
from multiprocessing import Pool, Manager

def copyFileTask(fileName, oldFileName, newFileName, queue) :
    "完成copy一个文件的功能"
    fr = open(oldFileName + '/' + name)
    fw = open(newFileName + '/' + name, w)

    content = f.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)

def main():
    
    #0. 获取用于要copy的文件夹的名字
    oldFileName = input('请输入文件夹的名字：')

    # 创建一个文件夹
    newFileName = oldFileName + '-复件'
    print(newFileName)
    os.mkdir(newFileName)

    # 获取old文件夹中给所有的文件名字
    fileNames = os.listdir(oldFileName)

    # 使用多进程的方式copy 原文件夹中的文件到新的文件夹中
    pool = Pool(5)
    queue = Manager().Queue()

    for fileName in fileNames:
        pool.apply_async(copyFileTask, args=(fileName, oldFileName, newFileName, queue))

    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num += 1
        copyRate = num/allNum
        print('\rcopy的进度是：%.2f%'%(copyRate*100), end='')
        if num == allNum:
            break
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
