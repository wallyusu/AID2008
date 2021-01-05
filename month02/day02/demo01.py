"""
    常用命令：
        cd  mkdir   rm  cat
        touch   grep    wc  cp  mv

        zip
        tar

        sudo

        find
        find    /home/tarena    -name
"""

"""
    用数字改权限
    echo
    echo -n 'hello world'
"""

"""
    Linux 总结
        1.Linux 操作系统的构成 特点  应用场景
        2.掌握    文件结构    绝对路径    相对路径
        3.掌握Linux的常用命令
        4.压缩解压  创建用户    远程访问    软件安装
        5.使用vi 进行简单的文本编辑
        简历要求：能够熟练使用Linux系统环境
"""
"""
作业：1.今天的命令  操作一下
     2.vi 编写    求100000以内的指数之和
     质数：除了1和其本身不能被其他数整除的数
"""

# result = []
num = 0
for i in range(2,1000):
    for j in range(2,i):
        if i % j == 0:
            break
        # result.append(i)
        num += i

print(num)

