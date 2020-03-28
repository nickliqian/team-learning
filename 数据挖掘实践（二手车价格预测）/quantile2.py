import pandas as pd
import numpy as np


def box_plot_outliers(data_ser, box_scale):
    """
    利用箱线图去除异常值
    :param data_ser: 接收 pandas.Series 数据格式
    :param box_scale: 箱线图尺度，
    :return:
    """
    # 3/4分位 - 1/4分位的差，乘上缩放尺度
    iqr = box_scale * (data_ser.quantile(0.75) - data_ser.quantile(0.25))
    val_low = data_ser.quantile(0.25) - iqr  # 离群值下限值
    val_up = data_ser.quantile(0.75) + iqr  # 离群值上限值
    rule_low = (data_ser < val_low)  # 筛选过大和过小的离群值为False
    rule_up = (data_ser > val_up)
    return (rule_low, rule_up), (val_low, val_up)


s = pd.Series([-567, -367, -300, 1, 2, 3, 4, 23, 26, 40, 56, 78, 79, 84, 90, 95, 150, 345, 785, 346, 436])

a, b = box_plot_outliers(s, 3)

print(b)
print(a)



print(np.arange(s.shape[0])[a[0] | a[1]])
