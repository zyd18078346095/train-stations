# -*- encoding: utf-8 -*-

"""
 获取全国车站中文名和英文简称

 Author: zsyoung

 Date: 2019/01/09 15:00
"""
import requests

response = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9090")
# 将信息头部和尾部删掉
data_str = response.text.strip("var station_names =';")
# 使用@符号分割成列表（为什么要用@？可查看具体数据）
data_list = data_str.split("@")[1:]
data_dict = {}
# 遍历列表
for item in data_list:
    # 再次使用|分割
    list_temp = item.split("|")
    # 存入字典
    data_dict[list_temp[1]] = list_temp[2]


# def save(re):
#     file = open("stationName.txt", "w")
#     for k, v in re.items():
#         print(k, v)
#         # line = k.encode("utf-8") + "\t" + str(v) + "\n" + str(k) + "\n"
#         line = k.encode("utf-8") + "\n" + str(v)
#         file.write(line)
#     file.close()

# save(data_dict)

# 打印出的车站字典直接复制粘贴到Constant.py中STATION_DICT即可
print(data_dict)
