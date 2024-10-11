'''
绘制简单的散点图
'''

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)  # 参数s设置绘制图形时使⽤的点的尺⼨
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)  # 参数c设置散点图点的颜色,将其设置为⼀个元组，
                                                       # 其中包含三个0〜1的⼩数值，分别表⽰红⾊、绿⾊和蓝⾊的分量。
                                                       # 值越接近0，指定的颜⾊越深；值越接近1，指定的颜⾊越浅。
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # 根据每个点的y值来设置其颜⾊渐变

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值得平方", fontsize=14)

# 设置刻度标记的⼤⼩。
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 1100000])  # x和y坐标轴的最⼩值和最⼤值。这⾥将x坐标轴的取值范围设置为0〜1100，并将y坐标轴的取值范围设置为0〜1 100 000

# 设置 y 轴不使用科学计数法
ax.ticklabel_format(style='plain', axis='y')

plt.show()

# ⾃动保存图表
# plt.savefig('squares_plot.png', bbox_inches='tight')  # 第⼆个实参指定将图表多余的空⽩区域裁剪掉，如果要保留图表周围多余的空⽩区域，只需省略这个实参即可。