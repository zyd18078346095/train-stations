# -*- encoding: utf-8 -*-

"""
 获取火车车次及沿途停靠站点信息

 Author: zsyoung

 Date: 2019/01/09 15:00
"""
import json


def parse_train_no_json(train_no_json):
    """
    解析火车车次信息json，获取火车车次
    :param train_no_json: 火车车次信息json
    :return: 火车车次列表
    """
    train_no_list = []
    json_text = json.loads(train_no_json)
    data = json_text['data']
    result = data['result']
    for r in result:
        list_temp = r.split("|")
        if list_temp.__contains__("预订"):
            train_no = list_temp[list_temp.index("预订") + 1]
            train_no_list.append(train_no)
    return train_no_list


def parse_station_info_json(station_info_json):
    """
    解析沿途停靠站点信息
    :param station_info_json: 车站信息json
    :return: [简略火车车次, 起点站名, 终点站名]
    """
    json_text = json.loads(station_info_json)
    data = json_text['data']['data']
    start_station_name = data[0]['start_station_name']
    station_train_code = data[0]['station_train_code']
    train_class_name = data[0]['train_class_name']
    service_type = data[0]['service_type']
    end_station_name = data[0]['end_station_name']
    # for d in data:
    #     arrive_time = d['arrive_time']
    #     station_name = d['station_name']
    #     start_time = d['start_time']
    #     stopover_time = d['stopover_time']
    #     station_no = d['station_no']

    return [station_train_code, start_station_name, end_station_name]
