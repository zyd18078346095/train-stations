# -*- encoding: utf-8 -*-

"""
 12306网爬虫Main
 
 Author: zsyoung
 
 Date: 2019/01/09 15:00
"""

import threading
import stationcrawl.threadpool as threadpool
import time
from stationcrawl import HttpUtils, FileUtils
from stationcrawl.Constants import *
from stationcrawl.TrainSpider import parse_train_no_json
from stationcrawl.TrainSpider import parse_station_info_json
from stationcrawl.ArgList import build_all_list
from stationcrawl.ArgList import get_key
from stationcrawl.StationDict import station_dict

mutexLock = threading.Lock()


def start(arg):
    print("arg:", arg)
    print('【' + threading.current_thread().name + ' -> start】')

    """先抓取火车车次信息json"""
    train_no_url = TRAIN_NO_BASE_URL + 'leftTicketDTO.train_date=' + str(arg[0]) + '&leftTicketDTO.from_station=' + str(
        arg[1]) + '&leftTicketDTO.to_station=' + str(arg[2]) + PURPOSE_CODES
    print("train_no_url:", train_no_url)
    train_no_text = HttpUtils.get_bytes(train_no_url)
    # print(train_no_text)

    """根据获取的火车车次，查询沿途车站停靠信息"""
    for train_no in parse_train_no_json(train_no_text):
        station_info_url = STATION_INFO_BASE_URL + 'train_no=' + train_no + '&from_station_telecode=' + str(
            arg[1]) + '&to_station_telecode=' + str(arg[2]) + '&depart_date=' + str(arg[0])
        print("station_info_url:", station_info_url)
        station_info_text = HttpUtils.get_bytes(station_info_url)
        # 解析沿途停靠站点信息
        station_info_list = parse_station_info_json(station_info_text)
        # 如果到达站点不是这趟列车的终点，就不保存这趟列车数据，防止爬重复
        if arg[2] != station_dict[station_info_list[2]]:
            return
        else:
            # 格式化车次，出发站，到达站
            simple_train_no = station_info_list[0]
            from_station = get_key(station_dict, arg[1])
            to_station = get_key(station_dict, arg[2])
            print(threading.current_thread().name + ' ->', [simple_train_no, from_station, to_station])
            # 存储为json文件，一个地址一个文件夹，不用考虑并发问题，不用加锁
            path = DIR_NAME + '/' + arg[0] + '/' + from_station + '/' + to_station + '/' + simple_train_no + '.json'
            FileUtils.save_file(path, station_info_text)

            # mutexLock.acquire()
            # 需要加锁的方法
            # mutexLock.release()
            # 暂停一下，再爬
            time.sleep(SLEEP_TIME)

    print('【' + threading.current_thread().name + ' -> over】')


if __name__ == '__main__':
    pool = threadpool.ThreadPool(THREAD_COUNT)
    requests = threadpool.makeRequests(start, build_all_list())
    [pool.putRequest(req) for req in requests]
    pool.wait()

    print('---stationcrawl over---')
