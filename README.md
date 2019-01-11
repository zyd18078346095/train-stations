# 12306爬虫
**注：爬取[12306网](https://kyfw.12306.cn)上的车次信息的爬虫，仅供交流学习之用，请勿用于商业用途**

## **项目地址：https://gitee.com/zsyoung01/train**

## 介绍
12306爬虫，抓取指定城市，始发和经过的所有车次信息

## 特性
1. 网络请求-数据解析-文件存储 三层结构
2. 多线程下载
3. 网络自动重试
4. 错误日志记录
5. Python3

## 你可能需要
- pip3 install requests
- pip3 install json
- pip3 install datetime
- pip3 install threadpool
- pip3 install retrying

## 项目结构
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190111114612388.png)

## 代码说明
- Main.py -> 主程序入口，业务处理
- TrainSpider.py -> 爬虫json解析
- GetAllStation.py -> 获取所有车站
- ArgList.py -> 参数列表构建
- threadpool.py -> 线程池工具
- HttpUtils.py -> 网络请求工具
- FileUtils.py -> 文件保存工具
- LogUtils.py -> 日志工具
- Constants.py -> 常量设置

## 使用说明
1. 本次爬虫只抓取经过和始发重庆的车次信息，如果需要全国的车次信息可以在ArgList.py中更改from_station = STATION_DICT
2. 本次爬虫默认抓取车次时间为明天，如果需要更改时间，可以在ArgList.py中更改train_date，格式为'2019-01-01'
3. 参数调整完之后直接启动Main.py即可

## LICENSE
```
 Copyright 2019 zsyoung

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```

