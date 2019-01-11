# -*- encoding: utf-8 -*-

"""
 构建参数列表以及根据value反向获取key方法

 Author: zsyoung

 Date: 2019/01/09 15:00
"""
from stationcrawl.StationDict import station_dict
from stationcrawl.Constants import TRAIN_DATE

to_station = station_dict
from_station = {'重庆北': 'CUW', '重庆': 'CQW', '重庆南': 'CRW', '重庆西': 'CXW'}
date = TRAIN_DATE


def build_all_list():
    """
    构建参数列表
    :return: [[出发日期，出发车站，到达车站]]
    """
    all_list = []
    for i in from_station.values():
        for j in to_station.values():
            new_list = [date, i, j]
            all_list.append(new_list)
    print(all_list)
    return all_list


def get_key(dict, value):
    """
    根据字典value获取key
    :param dict:
    :param value:
    :return: key
    """
    for k, v in dict.items():
        if v == value:
            return k
