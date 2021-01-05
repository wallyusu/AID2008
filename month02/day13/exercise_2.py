from multiprocessing import Pool,Queue
from time import sleep,ctime
import random
import os

def get_size(dir):
    total_getsize = os.listdir(dir)


# 拷贝每一个文件 --》 进程池要做的事情
def copy(filename,old_folder,new_folder):
    fr = open(old_folder+"/"+filename,'rb')
    fw = open(new_folder+"/"+filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()



# 创建进程池 参数为要拷贝的目录
def main(old_folder):
    # 创建新文件夹
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)

    pool = Pool(4)
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,
                         args=(file,old_folder,new_folder))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main("/home/tarena/FTP")