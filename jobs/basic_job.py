import libs.common as common
import pandas as pd
import tushare as ts

def stat_all(tmp_datatime):
    data = ts.get_deposit_rate()
    common
