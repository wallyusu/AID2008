"""
群聊聊天室
功能 ： 类似qq群功能
【1】 有人进入聊天室需要输入姓名，姓名不能重复

【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室

【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx

【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室

【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
"""
"""
1.需求分析
2.技术分析
3.功能模块划分、封装方法
4.网络协议设置
5.功能模块逻辑具体分析
6.优化完善

技术分析    c/s
存储人员信息：服务器
    存什么: 名字 地址
    怎么存： {name:address}
            [(name,address),...]
            class Person:
                def __init__(self,name,address):
                    self.name = name
                    self.address = address
                    
消息的网络传递：udp
    消息发送： 转发的方法     客户端 -> 服务端 -> 客户端
    收发消息： 多进程，一个负责发送，一个负责接收
    
功能模块划分 封装方法 函数封装
    框架模型
        服务端： 1.创建udp网络服务端
                2.循环接收各种客户端请求
                3.根据请求做出调用
        客户端： 1.创建udp网络
    进入聊天室
        客户端：1.输入姓名
               2.发送给服务端
               3.接收服务端反馈
               4.Y 进入聊天室    N 回到第一步
               
        服务端：1.接收请求
               2.判断是否有这个姓名
               3.根据判断发送结果
                    Y -> 存储用户   告知其他人
                    N -> over
    聊天
        客户端：1.创建子进程
               2.父进程循环发送消息
                 子进程循环接收消息
        
        服务端：1.接收请求
               2.将消息转发给其他人
        
    退出聊天室
    
网络协议设置
            请求类型      数据参量
    进入     LOGIN        name
    聊天     CHAT         说话的内容
    退出     EXIT 

"""
