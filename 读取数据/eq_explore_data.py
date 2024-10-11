import json
import plotly.express as px
import pandas as pd

# 探索数据的结构。
filename = r'C:\Users\45075\Desktop\zqq\code_cs\学习\项目\数据可视化\读取数据\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  # 将数据转换为Python能够处理的格式

# readable_file = r'C:\Users\45075\Desktop\zqq\code_cs\学习\项目\数据可视化\读取数据\data\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)  # 接受⼀个JSON数据对象和⼀个⽂件对象，并将数据写⼊这个⽂件中
                                         # 参数 indent=4 指定生成的 JSON 数据的缩进空格数

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])

data = pd.DataFrame(
 data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"]
)  # zip 函数将每个列表中相同索引位置的元素打包成一个元组，然后将这些元组组合成一个迭代器
# print(data.head())

fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
    color="震级",
    hover_name="位置",
)
# fig.write_html("global_earthquakes.html")
fig.show()

# fig = px.scatter(
#     x=lons,
#     y=lats,
#     labels={"x": "经度", "y": "纬度"},
#     range_x=[-200, 200],
#     range_y=[-90, 90],
#     width=800,
#     height=800,
#     title="全球地震散点图",
# )
# fig.write_html("global_earthquakes.html")
# fig.show()