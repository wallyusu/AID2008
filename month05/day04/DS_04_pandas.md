# 一、泰坦尼克号生存预测分析

大家都熟悉的Jack and Rose的故事，豪华游艇倒了，大家都惊恐逃生，可是救生艇的数量有限，副船长说lady and kid first！，所以是否获救其实并非随机，而是基于一些背景有先后顺序的。

今日目标：对数据进行描述性分析，探索性分析，构建特征，数据预处理

后续：训练和测试数据是一些乘客的个人信息以及存活状况，要尝试根据它生成合适的模型并预测其他人的存活状况。 

## 1. 项目步骤

\- 简单分析方法：（现状分析或问题定位）掌握数理统计等知识完成基础的业务数据分析，提取有价值的信息，形成有效的结论。比如：描述性统计分析，探索性数据分析

 \- 深层业务逻辑建模分析：（未来数据预测）使用数据挖掘算法中的分类、聚类、回归等方法搭建模型，分析完成复杂的数据分析工作，重点挖掘数据价值，寻找模式与规律。 

本项目步骤

1. 读取数据
2. 数据的简单描述性分析
3. 通过可视化的方式深入了解数据中的特征
4. 查看每一个属性与获救情况的可视化，找到与结果有关的特征
5. 数据预处理：包含缺失值处理，one-hot处理，标准化处理

## 2. 描述性统计分析概念

描述性统计分析：描述性统计分析要对调查总体所有变量的有关数据做统计性描述，主要包括数据的集中趋势分析、数据离散程度分析、数据的频数分析

1. 集中趋势的描述性统计量

- 均值：是指一组数据的算术平均数，描述一组数据的平均水平，是集中趋势中波动最小、最可靠的指标，但是均值容易受到极端值（极小值或极大值）的影响。
- 中位数：是指当一组数据按照顺序排列后，位于中间位置的数，不受极端值的影响，对于定序型变量，中位数是最适合的表征集中趋势的指标。
- 众数：是指一组数据中出现次数最多的观测值，不受极端值的影响，常用于描述定性数据的集中趋势
2. 离散程度的描述性统计量
- 最大值和最小值：是一组数据中的最大观测值和最小观测值
- 极差：又称全距，是一组数据中的最大观测值和最小观测值之差，记作R，一般情况下，极差越大，离散程度越大，其值容易受到极端值的影响。
- 方差和标准差：是描述一组数据离散程度的最常用、最适用的指标，值越大，表明数据的离散程度越大。
3. 频数分析
- 对列进行 频数分布分析，需要区分数值型数据和类别型数据的分析方式  频数分布分析（又称频率分析）主要通过频数分布表、条形图和直方图、百分位值等来描述数据的分布特征。

## 3. 探索性统计分析概念

1. 探索性分析由约翰·图基(john Tukey)在20世纪70年代开发，经常被描述为一种哲学，对于如何进行分析没有硬性规定，在统计学上，EDA是指通过分析数据，来总结数据主要特征的方法，可视化方法是使用较多的方式

2. 这个过程并不一定需要统计模型，EDA的主要目的是在尽量少的先验假设下，心无杂念的让数据告诉我们一切，使用可视化和定量方法来了解数据所讲述的故事，在其中寻找线索、逻辑、问题或研究领域等线索。

3.  主要目的：

   1、寻找数据特征之间的关系、鉴别特征之间有趣的或者意想不到的关系

    2、分析并希望找出与结果有关的特征，进而完成特征工程的构建

    3、是否需要更多数据做数据分析的支撑

## 4. 泰坦尼克号数据描述性分析

本次目的：对泰坦尼克号训练接数据进行描述性分析

主要包含：读取数据并对列进行分析

1. 获救情况人数可视化
2. 乘客等级分布可视化
3. 各登船口岸上船人数可视化
4. 性别分布
### (1)、DataFrame的plot绘图方法

![2](img\2.png)使用DataFrame的plot方法绘制图像会按照数据的每一列绘制一条曲线，参数中的columns就是列的名称而index本来是DataFrame的行名称。图形绘制成功之后还会按照列的名称绘制图例

参考链接：https://blog.csdn.net/brucewong0516/article/details/80524442这个功能确实是比较赞的。如果使用matplotlib的基本绘制功能，图例的添加还需要自己额外处理。看来，数据的规整化不仅仅是为了向量化以及计算加速做准备，而且为数据的可视化提供了不少便捷的方法。

kind参数：

‘line’ : line plot (default)#折线图

‘bar’ : vertical bar plot#柱状图

‘barh’ : horizontal bar plot#横向条形图

‘hist’ : histogram#直方图

‘box’ : boxplot#箱线图

‘kde’ : Kernel Density Estimation 密度估计图

‘pie’ : pie plot#饼图

‘scatter’ : scatter plot#散点图

#### 代码练习：DataFrame_plot.ipynb

```Python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
np.random.seed(123)
df=pd.DataFrame(np.random.randn(3,4),index=[1,2,3],columns=list('MNJK'))
df
df.plot()
# 同时画多个子图，可以设置 subplots = True
df.plot(subplots=True,figsize=(6,6))
fig=plt.figure(figsize=(10,6))
ax1=fig.add_subplot(2,1,1)
df.plot('M','J',ax=ax1,grid=True,style='-',title='random',xticks=range(4),yticks=range(4),rot=20,kind='line')
ax2=fig.add_subplot(2,1,2)
df.plot('N','K',ax=ax2,grid=True,xticks=range(5),yticks=range(5),rot=20,kind='scatter')
```
### (2)、数据描述性统计分析

代码目标：对数据进行读取并做描述性分析
#### 代码位置：Titanic_analysis.ipynb

```python
#一：读取数据
# 导入环境库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 正常显示中文
plt.rcParams['font.sans-serif']=['SimHei']
# 正常显示符号
plt.rcParams['axes.unicode_minus']=False
data_train=pd.read_csv('data/train.csv')
data_train
#二：对数据做描述性统计分析
# 完整性分析
data_train.info()
# 数值型数据描述分析
data_train.describe()
# 类别型数据描述分析
# data_train.select_dtypes('object').describe().T
#1、获救情况人数可视化
data_Survived=data_train.Survived.value_counts()
data_Survived
data_train.Survived.value_counts().plot(kind='bar',
                                        rot=0,
                                        figsize=(6,6),
                                        fontsize=18,
                                        color=['b','r'])
plt.title('获救情况人数可视化',fontsize=20)
plt.xlabel('获救情况',fontsize=15)
plt.ylabel('人数',fontsize=15)
for a,b in zip(data_Survived.index,data_Survived.values):
    plt.text(a,b,'%.0f'%b,ha='center',va='bottom',fontsize=15)
# 2、各登船口岸人数可视化
data_train.Embarked.value_counts()
data_train.Embarked.value_counts().plot(kind='bar',
                                        rot=0,
                                        figsize=(6,6),
                                        fontsize=18)
plt.title('登船口岸人数可视化',fontsize=20)
# 3、乘客等级人数可视化
data_train.Pclass.value_counts()
data_train.Pclass.value_counts().plot(kind='bar',
                                        rot=0,
                                        figsize=(6,6),
                                        fontsize=18)
plt.title('乘客等级人数可视化',fontsize=20)
# 4、性别分布
data_train.Sex.value_counts()
data_train.Sex.value_counts().plot(kind='bar',
                                        rot=0,
                                        figsize=(6,6),
                                        fontsize=18)
plt.title('性别分布可视化',fontsize=20)
```

### (3)、数据探索性分析

1. 各乘客等级的获救情况
2. 看看各性别的获救情况
3. 查看各登船港口的获救情况
4. 堂兄弟和父母字段对于获救情况分析
5. 分析cabin这个值的有无，对于survival的分布状况
6. 分析票价

```python
#1、分析各等级乘客年龄分布情况
plt.figure(figsize=(8,6))
data_train.Age[data_train.Pclass==1].plot(kind='kde',fontsize=15)
data_train.Age[data_train.Pclass==2].plot(kind='kde',fontsize=15)
data_train.Age[data_train.Pclass==3].plot(kind='kde',fontsize=15)
plt.xlabel('年龄',fontsize=15)
plt.ylabel('密度',fontsize=15)
plt.title('各等级乘客年龄分布情况',fontsize=18)
plt.legend(['一等舱','二等舱','三等舱'],fontsize=14)
# 查看各乘客等级的获救情况
# 未获救情况统计
survived_0=data_train.Pclass[data_train.                            Survived==0].value_counts()
# 获救情况统计
survived_1=data_train.Pclass[data_train.                             Survived==1].value_counts()
# survived_1
df_pclass=pd.DataFrame({'获救':survived_1,
            df_pclass.plot(kind='bar',fontsize=15,rot=0,figsize=(8,6))
plt.xlabel('乘客等级',fontsize=15)
plt.ylabel('人数',fontsize=15)
plt.title('各乘客等级的获救情况分析',fontsize=18)
                        #'未获救':survived_0})
df_pclass
df_pclass.plot(kind='bar',fontsize=15,rot=0,figsize=(8,6))
plt.xlabel('乘客等级',fontsize=15)
plt.ylabel('人数',fontsize=15)
plt.title('各乘客等级的获救情况分析',fontsize=18)
# 查看各性别的获救情况
survived_0=data_train.Sex[data_train.Survived==0].value_counts()
survived_0
survived_1=data_train.Sex[data_train.survived==1].value_counts()
survived_1
df_Sex=pd.DataFrame({'获救':survived_1,'未获救':survived_0})
df_Sex
df_Sex.plot(kind='bar',rot=0,fontsize=15,figsize=(8,6))
rate_sex=df_Sex['获救']/(df_Sex['获救']+df_Sex['未获救'])
rate_sex=np.round(rate_sex,2)
df_Sex['rate_sex']=rate_sex
df_Sex
# 查看各登船港口的获救情况
survived_0=data_train.Embarked[data_train.
                          Survived==0].value_counts()
survived_0
survived_1=data_train.Embarked[data_train.
                          Survived==1].value_counts()
survived_1
df_Embarked=pd.DataFrame({'获救':survived_1,'未获救':survived_0})
df_Embarked
rate_Embarked=df_Embarked['获救']/(df_Embarked['获救']+df_Embarked['未获救'])
rate_Embarked=np.round(rate_Embarked,2)
df_Embarked['rate_Embarked']=rate_Embarked
df_Embarked
# 堂兄弟和父母字段对于获救情况分析
# （1）有无兄弟姐妹/父母子女和存活与否的关系
# 根据题目要求，分四种情况（有无兄弟，有无父母）计算存活率。
# 先进行数据筛选。
sib_data = data_train[data_train['SibSp'] != 0]
# sib_data
nosib_data = data_train[data_train['SibSp'] == 0]
par_data = data_train[data_train['Parch'] != 0]
nopar_data = data_train[data_train['Parch'] == 0]
sib_data['Survived'].value_counts()
fig=plt.figure(figsize = (16,4))
# #有无兄弟姐妹的存活率对比
ax1=fig.add_subplot(141)
plt.axis('equal')
sib_data['Survived'].value_counts().plot(kind='pie',labels = ['No Survived','Survived'],autopct = '%.2f%%',colormap = 'Blues')
plt.xlabel('sibsp')

ax2=fig.add_subplot(142)
plt.axis('equal')
nosib_data['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],autopct = '%.2f%%',colormap = 'Blues')
plt.xlabel('no_sibsp')
#有无父母子女的存活率对比
ax3=fig.add_subplot(143)
plt.axis('equal')
par_data['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],autopct = '%.2f%%',colormap = 'Reds')
plt.xlabel('parch')

ax4=fig.add_subplot(144)
plt.axis('equal')
nopar_data['Survived'].value_counts().plot.pie(labels = ['No Survived','Survived'],autopct = '%.2f%%',colormap = 'Reds')
plt.xlabel('no_parch')
# cabin有没有值对于获救情况的影响
# 有cabin记录的数据
survived_cabin=data_train.Survived[pd.notnull(data_train.Cabin)].value_counts()
# 没有cabin记录的数据
survived_nocabin=data_train.Survived[pd.isnull(data_train.Cabin)].value_counts()
survived_nocabin
df_cabin=pd.DataFrame({'有':survived_cabin,'无':survived_nocabin}).T
df_cabin
rate_cabin=df_cabin[1]/(df_cabin[0]+df_cabin[1])
rate_cabin=np.round(rate_cabin,2)
df_cabin['rate_cabin']=rate_cabin
df_cabin
# 分析票价
fare_die = data_train['Fare'][data_train['Survived'] == 0]
fare_sur = data_train['Fare'][data_train['Survived'] == 1]
fare_die.describe()
fare_sur.describe()
```

# 二、pandas数据预处理

1.数据缺失值处理：age，Cabin，Embarked  -------数据清洗 

2.数据one-hot处理：逻辑回归算法需要传入的数据是数值型-------转换数据

3.数据标准化处理：对数据进行标准化处理-------标准化数据

## 1. 合并数据

### (1)、横向堆叠合并数据  

当axis=1的时候，concat做横向合并

当两张表完全一样时，不论join参数取值是inner或者outer，结果都是将两个表完全按照X轴拼接起来。

![concat1](img\concat1.png)

![concat2](img\concat2.png)

1. 横向表堆叠
   横向堆叠，即将两个表在X轴向拼接在一起，可以使用concat函数完成，concat函数的基本语法如下：

   | 参数名称         | 说明                                                         |
   | ---------------- | ------------------------------------------------------------ |
   | objs             | 接收多个Series，DataFrame的组合。表示参与连接的pandas对象的列表的组合。无默认。 |
   | axis             | 接收0或1。表示连接的轴向，默认为0。                          |
   | join             | 接收inner或outer。表示其他轴向上的索引是按交集（inner）还是并集（outer）进行合并。默认为outer。 |
   | join_axes        | 接收Index对象。表示用于其他n-1条轴的索引，不执行并集／交集运算。 |
   | ignore_index     | 接收boolean。表示是否不保留连接轴上的索引，产生一组新索引range(total_length)。默认为False。 |
   | keys             | 接收sequence。使用传递的键作为最外层来构造层次索引。加上一个层次的key来识别数据源自于哪张表，区分不同的表数据来源，默认为None。 |
   | names            | 接收list。生成的层次结构索引中的级别的名称。默认为None。     |
   | verify_integrity | 接收boolearn。表示是否检查结果对象新轴上的重复情况，如果发现则引发异常。默认为False。 |
### (2)、纵向堆叠合并数据  

当axis=0的时候，concat做纵向合并

![concat3](img\concat3.png)
![concat3](img\concat4.png)
![concat3](img\concat5.png)

纵向堆叠——append方法

append方法也可以用于纵向合并两张表。但是append方法实现纵向表堆叠有一个前提条件，那就是两张表的列名需要完全一致。append方法的基本语法如下

| 参数名称         | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| other            | 接收DataFrame或Series。表示要添加的新数据。无默认。          |
| ignore_index     | 接收boolean。如果输入True，会对新生成的DataFrame使用新的索引（自动产生）而忽略原来数据的索引。默认为False。 |
| verify_integrity | 接收boolean。如果输入True，那么当ignore_index为False时，会检查添加的数据索引是否冲突，如果冲突，则会添加失败。默认为False。 |

#### 代码练习  concat_append.ipynb

```Python
import numpy as np
import pandas as pd
#定义资料集
df1 = pd.DataFrame(np.ones((3,4))0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
# conca基本参数练习
#res接收 concat纵向合并   注意参数axis合并方向
# res=pd.concat(objs=[df1,df2,df3],axis=0)
# res
#承上一个例子，并将并将ignore_index设定为True：重置index
res=pd.concat(objs=[df1,df2,df3],axis=0,ignore_index=True)
res
#concat_join参数的练习
# join (合并方式) 如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集
#定义资料集
df1 = pd.DataFrame(np.ones((3,4))0,columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))1,columns=['b','c','d','e'], index=[2,3,4])
# join (合并方式) 如果为’inner’得到的是两表的交集，如果是outer，得到的是两表的并集
res=pd.concat(objs=[df1,df2],axis=0,join='outer',sort=True,keys=['df1','df2'],names=['df_name','row_id'])
res
# 内合并
res=pd.concat(objs=[df1,df2],axis=0,join='inner',ignore_index=True)
res
# append合并案例练习
# append合并
#定义资料集
df1 = pd.DataFrame(np.ones((3,4))0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))1, columns=['a','b','c','d'])
#要求将df2合并到df1的下面，以及重置index，并打印出结果
df1.append(df2,ignore_index=True)
```
## 2. 清洗数据
### (1)、检测与处理缺失值
- 利用isnull或notnull找到缺失值
- 数据中的某个或某些特征的值是不完整的，这些值称为缺失值。
- pandas提供了识别缺失值的方法isnull以及识别非缺失值的方法notnull，这两种方法在使用时返回的都是布尔值True和False。
- 结合sum函数和isnull、notnull函数，可以检测数据中缺失值的分布以及数据中一共含有多少缺失值。isnull和notnull之间结果正好相反，因此使用其中任意一个都可以判断出数据中缺失值的位置。
#### 1、删除法
删除法分为删除观测记录和删除特征两种，它属于利用减少样本量来换取信息完整度的一种方法，是一种最简单的缺失值处理方法。
pandas中提供了简便的删除缺失值的方法dropna，该方法既可以删除观测记录，亦可以删除特征。
pandas.DataFrame.dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)

| 参数名称 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| axis     | 接收0或1。表示轴向，0为删除观测记录（行），1为删除特征（列）。默认为0。 |
| how      | 接收特定string。表示删除的形式。any表示只要有缺失值存在就执行删除操作。all表示当且仅当全部为缺失值时执行删除操作。默认为any。 |
| subset   | 接收类array数据。表示进行去重的列∕行。默认为None，表示所有列/行。 |
| inplace  | 接收boolean。表示是否在原表上进行操作。默认为False。         |
#### 2、替换法
- 替换法是指用一个特定的值替换缺失值。
- 特征可分为数值型和类别型，两者出现缺失值时的处理方法也是不同的。
- 缺失值所在特征为数值型时，通常利用其均值、中位数和众数等描述其集中趋势的统计量来代替缺失值。
- 缺失值所在特征为类别型时，则选择使用众数来替换缺失值

![fillna](img\fillna.png)
pandas库中提供了缺失值替换的方法名为fillna，其基本语法如下。pandas.DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None)

| 参数名称 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| value    | 接收scalar，dict，Series或者DataFrame。表示用来替换缺失值的值。无默认。 |
| method   | 接收特定string。backfill或bfill表示使用下一个非缺失值填补缺失值。pad或ffill表示使用上一个非缺失值填补缺失值。默认为None。 |
| axis     | 接收0或1。表示轴向。默认为1。                                |
| inplace  | 接收boolean。表示是否在原表上进行操作。默认为False。         |
| limit    | 接收int。表示填补缺失值个数上限，超过则不进行填补。默认为None。 |

#### 代码练习：fillna_demo.ipynb

```python
import pandas as pd
import numpy as np
# 处理丢失数据
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
# df1接收，去掉有 NaN 的行, 可以使用 dropna 一旦出现NaN就去除整行
df1=df.dropna(axis=0,how='any')
df1
# df2接收，如果是将 NaN 的值用其他值代替, 比如代替成 0:
df2=df.fillna(value=0)
df2
# b列数据，填补平均值
df['B']=df['B'].fillna(df['B'].mean())
df
# c列数据，填补平均值
df['C']=df['C'].fillna(df['C'].mean())
df
# df3接收，判断是否有缺失数据 NaN, 为 True 表示缺失数据:
df3=df.isnull()
df3
#每一列的缺失数据
# df4=df.isnull().sum(axis=0)
# df4
#每一行的缺失数据
df5=df.isnull().sum(axis=1)
df5
#整个表的缺失数据
df5.sum()
```

## 3. 标准化数据
### (1)、离差标准化

![normalization1](img\normalization1.png)数据的整体分布情况并不会随离差标准化而发生改变，原先取值较大的数据，在做完离差标准化后的值依旧较大。

当数据和最小值相等的时候，通过离差标准化可以发现数据变为0。

### (2)、标准差标准化

![normalization2](img\normalization2.png)
#### 代码练习：normalization_demo.ipynb

```python
import numpy as np
import pandas as pd
np.random.seed(1)
df = pd.DataFrame(np.random.randn(4, 4)  4 + 3)
df
# 离差标准化
df_norm=(df-df.min())/(df.max()-df.min())
df_norm
# 标准差标准化
df_norm1=(df-df.mean())/(df.std())
df_norm1
```
## 4. 转换数据
### (1)、哑变量处理类别数据
数据分析模型中有相当一部分的算法模型都要求输入的特征为数值型，但实际数据中特征的类型不一定只有数值型，还会存在相当一部分的类别型，这部分的特征需要经过哑变量处理才可以放入模型之中。哑变量处理的原理示例如图

![dummies](img\dummies.png) Python中可以利用pandas库中的get_dummies函数对类别型特征进行哑变量处理。

pandas.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None)

| 参数名称   | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| data       | 接收array、DataFrame或者Series。表示需要哑变量处理的数据。无默认。 |
| prefix_sep | 接收string。表示前缀的连接符。默认为‘_’。                    |
| dummy_na   | 接收boolean。表示是否为Nan值添加一列。默认为False。          |
| columns    | 接收类似list的数据。表示DataFrame中需要编码的列名。默认为None，表示对所有object和category类型进行编码。 |
| prefix     | 接收string、string的列表或者string的dict。表示哑变量化后列名的前缀。默认为None。 |

哑变量处理特点

虚拟变量，也叫哑变量和离散特征编码，可用来表示分类变量、非数量因素可能产生的影响。

离散特征的编码分为两种情况：

- 离散特征的取值之间没有大小的意义，比如color：[red,green],那么就使用one-hot编码
- 离散特征的取值有大小的意义，比如size:[X,XL,XXL],那么就使用数值的映射{X:1,XL:2,XXL:3}
-  对于一个类别型特征，若其取值有m个，则经过哑变量处理后就变成了m个二元特征，并且这些特征互斥，每次只有一个激活，这使得数据变得稀疏。
-  对类别型特征进行哑变量处理主要解决了部分算法模型无法处理类别型数据的问题，这在一定程度上起到了扩充特征的作用。由于数据变成了稀疏矩阵的形式，因此也加速了算法模型的运算速度。

#### 代码练习：dummies.ipynb

```python
import pandas as pd  
df = pd.DataFrame([  
            ['green','M','10.2','class1'],
            ['red','L','13.5','class2'],  
            ['blue','XL','15.3','class1'],  
           ])  
df.columns = ['color','size','prize','class label'] 
df
df.info()
size_mapping={'XL':3,'L':2,'M':1}
df['size']=df['size'].map(size_mapping)
df
class_mapping={label:idx for idx,label in enumerate(set(df['class label']))}
class_mapping
df['class label']=df['class label'].map(class_mapping)
df
pd.get_dummies(df)
```

知识点补充： enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。 

代码练习：enumerate_test.ipynb

```pyth
seasons=['Spring','Summer','Fall','Winter']
list(enumerate(seasons))
list(enumerate(seasons,start=2))
# 普通for循环
i=0
seq=['one','two','three']
for element in seq:
    print (i,seq[i])
    i+=1
seq=['one','two','three']
for i,element in enumerate(seq):
    print(i,element)
```
### (2)、离散化连续型数据
- 某些模型算法，特别是某些分类算法如ID3决策树算法和Apriori算法等，要求数据是离散的，此时就需要将连续型特征（数值型）变换成离散型特征（类别型）。

- 连续特征的离散化就是在数据的取值范围内设定若干个离散的划分点，将取值范围划分为一些离散化的区间，最后用不同的符号或整数值代表落在每个子区间中的数据值。

- 因此离散化涉及两个子任务，即确定分类数以及如何将连续型数据映射到这些类别型数据上。其原理如图。

![cut](img\cut.png)

将数据的值域分成具有相同宽度的区间，区间的个数由数据本身的特点决定或者用户指定，与制作频率分布表类似。pandas提供了cut函数，可以进行连续型数据的等宽离散化，其基础语法格式如下。pandas.cut(x, bins, right=True, labels=None, retbins=False)

| 参数名称 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| x        | 接收数组或Series。代表需要进行离散化处理的数据。无默认。     |
| bins     | 接收int，list，array，tuple。若为int，代表离散化后的类别数目；若为序列类型的数据，则表示进行切分的区间，每两个数间隔为一个区间。无默认。 |
| right    | 接收boolean。代表右侧是否为闭区间。默认为True。              |
| labels   | 代表离散化后的各个类别名称                                   |
| retbins  | 接收boolean。代表是否返回区间标签。默认为False。             |

```python
import pandas as pd
ages=[20,22,34,56,34,12,9,43,23,18,45]
bins=[5,10,15,20,25,30,40,45,50,60]
cut_data=pd.cut(x=ages,bins=bins)
cut_data
cut_data.value_counts().plot(kind='barh')
```

## 5. 数据规约

分为属性规约和数值规约

在大数据集上进行复杂的数据分析和挖掘需要很长的时间，数据规约产生更小但保持数据完整性的新数据集，在规约后的数据集上进行分析和挖掘将更有效率

意义在于：

1. 降低无效，错误数据对建模的影响，提高建模的准确性
2.  少量且具有代表性的数据将大幅缩减数据挖掘所用的时间
3. 减低储存数据成本
### (1)、属性规约
通过属性合并来创建新属性维数，或者直接删除不相关的属性来减少数据维数，从而提高数据分析与挖掘的速度，目的是寻找最小的属性子集并确保新数据子集的概率分布尽可能的接近原来的数据集概率分布，常用方法见下表

![11](img\11.png)
### (2)、数值规约
- 指的是通过选择替代的，较小的数据来减少数据量，包括有参数，无参数方法

- 有参数：使用模型来评估数据，只存放参数，不存放实际数据 eg：线性回归/多元回归

- 无参数：存放实际数据，直方图/聚类/抽样

-    （1）直方图。如一连串的数据，通过绘制直方图（R中用hist()函数绘制直方图），分为“3~15”、“16~28”、“29~41”三个范围。
       （2）聚类。将对象划分为簇，使一个簇中的对象相互“相似”，而与其他簇中的对象“相异”，用数据的簇替换实际数据。
       （3）抽样。有放回/无放回

## 6. 泰坦尼克号数据预处理

1.数据缺失值处理：age，Cabin，Embarked  -------数据清洗 

2.数据one-hot处理：逻辑回归算法需要传入的数据是数值型-------转换数据

3.数据标准化处理：对数据进行标准化处理-------标准化数据

```python
# 缺失值处理 Age
data_train['Age']=data_train['Age'].fillna(data_train['Age'].mean())
# 缺失值处理 Embarked
data_train['Embarked']=data_train['Embarked'].fillna('S')
# 缺失值处理 Cabin
def set_cabin_type(df):
    df.loc[(df.Cabin.notnull()),'Cabin']='Yes'
    df.loc[(df.Cabin.isnull()),'Cabin']='No'
    return df
data_train1=set_cabin_type(data_train)
data_train1.info()
# 数据类型转换 类别型数据转换为数值型
dummies_Cabin=pd.get_dummies(data_train1['Cabin'],prefix='Cabin')
dummies_Sex=pd.get_dummies(data_train1['Sex'],prefix='Sex')
dummies_Embarked=pd.get_dummies(data_train1['Embarked'],prefix='Embarked')
dummies_Pclass=pd.get_dummies(data_train1['Pclass'],prefix='Pclass')
df=pd.concat([data_train1,dummies_Cabin,
              dummies_Embarked,dummies_Pclass,dummies_Sex],axis=1)
df.head()
df.columns
df.drop(['Pclass','Name','Ticket','Cabin','Embarked','Sex']
        ,axis=1,inplace=True)
# 数据标准化处理 Age,Fare
a=df.Age
df['Age_scaled']=(a-a.mean())/(a.std())
b=df.Fare
df['Fare_scaled']=(b-b.mean())/(b.std())
df.head()
df.drop('Age',axis=1,inplace=True)
```

