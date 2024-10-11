from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die(10)

# 掷⼏次骰⼦并将结果存储在⼀个列表中。
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进⾏可视化。
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'结果', 'dtick':1}  # 'dtick': 1 让Plotly显⽰每个刻度值。
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷⼀个D6和⼀个D10 50000次的结果',
                   xaxis=x_axis_config,yaxis=y_axis_config)  # 定义了图表的布局,布局包括了图表的标题和 x轴、y轴的配置
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')
