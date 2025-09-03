from typing import List
from chinese_calendar import is_workday
from datetime import datetime, date, timedelta
from dateutil.parser import parse

from dateutil.relativedelta import relativedelta


class XuanGu:
    def __init__(self, gongshi:str):
        self.gongshi = gongshi

    def get_workdays(self, start_date_str:str = None):
        first_day = parse(start_date_str).date() if start_date_str else date.today() - relativedelta(months=1)
        last_day = date.today()

        workdays = []
        current_date = last_day

        while current_date >= first_day:
            if is_workday(current_date) and current_date.weekday() < 5:
                workdays.append(current_date)
            current_date -= timedelta(days=1)
        return workdays

    def main(self, workdays: List[date]):
        if '前天' in self.gongshi:
            offset = 2
        elif '昨天' in self.gongshi:
            offset = 1
        else:
            offset = 0

        results = list()
        for workday_index in range(len(workdays) - offset):
            gongshi = self.gongshi.replace('今天',workdays[workday_index].strftime('%Y年%m月%d日'))
            if '昨天' in gongshi:
                gongshi = gongshi.replace('昨天',workdays[workday_index + 1].strftime('%Y年%m月%d日'))
            if '前天' in gongshi:
                gongshi = gongshi.replace('前天',workdays[workday_index + 2].strftime('%Y年%m月%d日'))
            gongshi = gongshi.replace(' ', ' ')

            results.append(gongshi)
        return results


if __name__ == '__main__':
    gongshi = '今天竞价涨幅小于6% 今天竞价大单净量大于0.2 小单流出大于1200万 中单流出大于400万 财务评分大于1.5 主板 非st 非s 非退市 非可转债 非港股'
    # gongshi = '今天竞价涨幅1.1%到3.5% 今天9点35分大单净量大于0.15 小单流出大于900万 中单流出大于300万 散户数量流出大于20 换手大于0.1 股价大于4元 非涨停 流通市值大于20亿 主板 非st 非s 非可转债 非退市 非港股 昨天非涨停 成交额大于1.4亿'
    # gongshi = '今天j大于昨天j加28 今天量比大于1.74 大单净量大于0.3 小单流出大于3000万 股价大于4 diff加0.1大于dea 财务评分大于1.5 主板 非st 非退市 非港股 非s 非可转债 流通市值大于20亿 昨天j小于d'
    # gongshi = '今天竞价涨幅4.4%到5.6%；今天大单净量大于0.25 小单流出大于2000万 主板 非st 非s 非可转债 昨天涨停取反'
    xuangu = XuanGu(gongshi)
    workdays = xuangu.get_workdays('2025-6-15')
    results = xuangu.main(workdays)
    for i in results:
        print(i)

'''
方案一： 弱转强，需要连板数大于等于2
最好的上车点是站稳均价线上方           
直线拉升不回踩就是没缘份  不能碰

炸板一次大于30分钟回封                次日直接核    
高开大于2%直接挂单                   次日直接核
平开无下影线才是真的强                次日开盘就砸不用慌，出货的话正常买点赚够10个点就离场
低开不砸地板  上午择机低吸            次日等待到尾盘

未涨停低开日内振幅大于11个点    次日不出货涨停预期，出货7个点预期
未涨停低开日内振幅小于11个点    次日预期3个点离场

资金高于前期的情况下还有2板预期  等一个尾盘封板
次日常规7个点预期，弱势5个点，高位非涨停横盘四分钟就是出货好时机
'''

'''
方案二：强势票
一档当天涨停不炸板、小炸：
    当天跌破0轴：
        次日直接核
    当天不破0轴：
        次日主力继续流入：
            等板不炸不动  次日还有溢价
        次日主力出货：
            高开大于5%    涨停减四档出
            平开小高开    7个点
            低开         5个点

大炸板                     次日直接核
一档当天不涨停              次日直接核
二档无论当天是否涨停         次日直接核
'''

'''
方案三：打首板
当天无炸板：
    次日高开大于5     直接挂涨停出
    次日小高开       7个点
    次日平开低开      1-3
'''

'''
常规首版
垃圾板直接核：
    11点之后板
    炸板
常规板：
    正常开     补3、5、7
    
    
崎岖
    



首版上午板 无炸板
次日平开   3个点预期
次日高开1-3  5个点预期
次日高开4-5  7个点预期
次日高开大于5 10个点预期
'''

