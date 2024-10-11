'''
绘制简单的折线图
'''

# import seaborn as sns
import matplotlib.pyplot as plt  # 模块pyplot 包含很多⽤于⽣成图表的函数

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# sns.set_style("whitegrid") 
fig, ax = plt.subplots()  # 变量fig 表⽰整张图⽚。变量ax 表⽰图⽚中的各个图表;subplots()函数可在⼀张图⽚中绘制⼀个或多个图表
ax.plot(input_values, squares, linewidth=3)  # linewidth 决定了plot() 绘制的线条粗细

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)  # 给图表指定标题;fontsize 指定图表中各种⽂字的⼤⼩。
ax.set_xlabel("值",  fontsize=14)  # 为x轴设置标题
ax.set_ylabel("值得平方", fontsize=14)  # 为y轴设置标题

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)  # 设置刻度的样式;（axes='both' ）影响x轴和y轴上的刻度;4（labelsize=14 ）将刻度标记的字号设置为14
plt.show()

