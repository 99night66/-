import csv
# import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

filename = r"C:\Users\45075\Desktop\zqq\code_cs\学习\项目\数据可视化\读取数据\data\sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 返回⽂件中的下⼀⾏ (只调⽤next() ⼀次，得到的是⽂件的第⼀⾏)

    # for index, column_header in enumerate(header_row):  # enumerate()来获取每个元素的索引及其值。
    #     print(index, column_header)

    # 从⽂件中获取最⾼温度。
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # 将字符串解析成日期时间对象
        high = int(row[5])
        highs.append(high)
        dates.append(current_date)

    # 根据最⾼温度绘制图形。
    # plt.style.use('seaborn-darkgrid')
    # sns.set_style('darkgrid')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # 设置图形的格式。
    ax.set_title("2018年每⽇最⾼温度", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 自动调整图表的x轴日期标签，以避免它们重叠
    ax.set_ylabel("温度 (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

