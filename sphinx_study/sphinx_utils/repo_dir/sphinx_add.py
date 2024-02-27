#!/usr/bin/env python3
# encoding: utf-8
# @author: firstelfin
# @time: 2024/02/27 10:00:27


from pydantic import BaseModel
from typing import Union, List, Dict, Optional


class SuppressParam(BaseModel):
    """

    :param abnormalNum:       默认None, # 上次异常上报后, 识别到的异常数量
    :type abnormalNum:        [int, None]
    :param suppressWinSize: 默认4     # 设置的异常周期, 单位小时
    :type suppressWinSize:  float
    :param lastTime:        默认0.0   # 上次异常上报请求的时间戳, 单位秒
    :type lastTime:         float
    :param maxEpoch:        默认2     # 最大重置周期
    :type maxEpoch:         int

    参数用于处理：

    :math: 
    
        `State(k,W,T_{s},T,\sigma) = I(k \times \Delta_{W} + \sigma \times (T_{s} + W - T) - 1 + \delta)`
    
    """

    abnormalNum:  Optional[int] = 0         # 上次异常上报后, 识别到的异常数量
    suppressWinSize:      float = 4         # 设置的异常周期, 单位小时
    lastTime:   Optional[float] = .0        # 上次异常上报请求的时间戳, 单位秒
    maxEpoch:     Optional[int] = 2         # 最大重置周期
    reqInterval:Optional[float] = 1         # 两次请求之间的时间间隔, 单位分钟
