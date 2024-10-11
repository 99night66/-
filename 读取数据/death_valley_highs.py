import csv
from datetime import datetime
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


filename = r"C:\Users\45075\Desktop\zqq\code_cs\学习\项目\数据可视化\读取数据\data\death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 返回⽂件中的下⼀⾏ (只调⽤next() ⼀次，得到的是⽂件的第⼀⾏)

    for index, column_header in enumerate(header_row):  # enumerate()来获取每个元素的索引及其值。
        print(index, column_header)