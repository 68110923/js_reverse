import json
import re
import time
import urllib.parse

import requests
import hashlib



class Configuration:
    appKey = '12574478'

    @staticmethod
    def get_sign(em_token: str, current_timestamp_milliseconds: str, app_key: str, ep_data: str):
        '''
        sign = eM
        eM = eE(em.token + "&" + eT + "&" + eC + "&" + ep.data)
        '''
        return hashlib.md5('&'.join([em_token, current_timestamp_milliseconds, app_key, ep_data]).encode('utf-8')).hexdigest()



url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
current_timestamp_milliseconds = str(int(time.time() * 1000))

# cookie, ua, search_params 这三个东西自己配置
cookie = 'cna=0z/PGhe3ByUCAXd7KbNtZt3e; t=21d4ccbf26aa107ab9e4306d8ecf1c79; mtop_partitioned_detect=1; _m_h5_tk=c862c5730a9cbcd62d6da9c202e37ec5_1756820251765; _m_h5_tk_enc=332169ed15ab23053b26782c594ca9ce; cookie2=1e0e870bfda6cd14645d62329e2fa330; _tb_token_=70408b5633753; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uetsid=05e3c2f087ed11f09abe5100d1dc90b6; _uetvid=05e3bbc087ed11f0b8bb795079ca1216; xlly_s=1; _samesite_flag_=true; sca=09aaff5f; 3PcFlag=1756811290307; sgcookie=E100l2CBjAcENDvqJY%2BgnWlB1cwWT3cldOON2Co4VzcFYT5g92if2Yr30pNnnMZ%2F29huomry09PSuDtIgCWd2pfoXzAmIAKk30f0kEiSh4aKp76GFlUhMvx1%2FYyEitrA%2FXVe; wk_cookie2=1eba9b6d00d0f0a2f0b84107b6a4ab7b; wk_unb=UUjViSS6wL6V6w%3D%3D; unb=2044787874; uc1=pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie21=UIHiLt3xSift4ZS1LW77rg%3D%3D&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie14=UoYbzWqy0BADjQ%3D%3D; uc3=id2=UUjViSS6wL6V6w%3D%3D&vt3=F8dD2fYMcZcFIP%2B3XU0%3D&nk2=ogcowdD1Py2B3HTRVJQybw%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; csg=a3757b40; lgc=%5Cu5218%5Cu5C55%5Cu78551515311352; cancelledSubSites=empty; cookie17=UUjViSS6wL6V6w%3D%3D; dnk=%5Cu5218%5Cu5C55%5Cu78551515311352; skt=8b1699ad8f3fb5d2; existShop=MTc1NjgxMTMwOA%3D%3D; uc4=id4=0%40U2o3vUuLe3Qvv2CZ5HJqDP%2BDX6LP&nk4=0%40oAWz1nZwfXlZ%2FV8vJi3SP1RGUZio%2BMVu7RFs; tracknick=%5Cu5218%5Cu5C55%5Cu78551515311352; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=24e; _nk_=%5Cu5218%5Cu5C55%5Cu78551515311352; cookie1=W8GPyKGJaKrS%2BODolYiIisWB6df0L%2BGkD9VOMwESwrc%3D; tfstk=gLkKLa1r3hIpCKQFv4AMEBPNluKGFCme-2ofEz4hNV3tVPXkYJAze4UtzyV3dyX8e03rr4nyYuaSP4UotCvmYDyzFE0JnKmeSKWiS2ECOOt72u5WjW_KAJSQFEYDnu6qBU2SrsNZYP1_0PZQVTZBX5ZuATw7Nki6XuZlR_6IPctT7kU5P9w51lZ4c8aSP8ttfPr7Fkg7Fhn_7uGtrLz1Rz6-OxzAXojGK_foBkFLyT4OeuMdn5UjAPBWQUZQ91mQWT6SCbLN8LzvBNaiVml76YpFK8oiM4hS5367yfZxko0HC9eS1VHYGc8ALyhs8Ye3gLI8XjnsJveJMMripcM4wv8dCy3Zfj2EhFW-lcmmL5kJkNartoy_vfK51yN54yDmHDi1olyOOhKOa_PQbrFBY7nQOr4TXrxpz_5zsFrTohLfa_PQblUDvH1Pa5YN.; isg=BMjIl8ZUNF1vmFjZ_ZKoeAYRmTDacSx7FusGVYJ7osOhXW3HKoVLCw4b1TUtxuRT',
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
search_params = {
    'q': urllib.parse.urlparse('厨具'),
    'page': 1,
    'pageSize': '48',
}
ep_data = json.dumps({
    'appId': '34385',
    'params': json.dumps({
        'areaCode': 'CN',
        'bcoffset': '',
        'brand': 'HUAWEI', 'categoryp': '', 'channelSrp': '', 'clientType': 'h5', 'client_os': 'Android',
        'countryNum': '156', 'couponUnikey': '', 'debug_rerankNewOpenCard': 'false', 'device': 'HMA-AL00',
        'elderHome': 'false', 'endPrice': None, 'end_price': None, 'filterTag': '', 'forceOldDomain': 'false',
        'from': 'nt_history', 'gpsEnabled': 'false', 'grayHair': 'false', 'ha3Kvpairs': None,
        'hasPreposeFilter': 'false',
        'homePageVersion': 'v7', 'index': '4', 'info': 'wifi', 'isBeta': 'false', 'isEnterSrpSearch': 'true',
        'isNewDomainAb': 'false', 'itemIds': None, 'loc': '', 'm': 'pc', 'myCNA': '0z/PGhe3ByUCAXd7KbNtZt3e', 'n': 48,
        'needTabs': 'true', 'network': 'wifi', 'newSearch': 'false', 'np': '', 'ntoffset': '', 'p4pIds': None,
        'p4pS': None,
        'page': search_params['page'], 'pageSize': search_params['pageSize'],
        'pageSource': 'a21bo.jianhua/a.201867-main.d5_fourth.37452a89vYcfXT',
        'prepositionVersion': 'v2', 'prop': '', 'q': search_params['q'], 'qSource': 'url', 'rainbow': '',
        'schemaType': 'auction', 'screenResolution': '1680x1050', 'searchDoorFrom': 'srp',
        'searchElderHomeOpen': 'false',
        'search_action': 'initiative', 'service': '', 'sort': '_coefp', 'sourceS': '0', 'startPrice': None,
        'start_price': None, 'style': 'list', 'subTabId': '', 'subtype': '', 'sugg': '_4_1', 'sversion': '13.6',
        'tab': 'all', 'totalPage': '100', 'totalResults': '326938', 'ttid': '600000@taobao_pc_10.7.0',
        'userAgent': ua,
        'vm': 'nw'
    })
})
sign = Configuration.get_sign(
    em_token='c862c5730a9cbcd62d6da9c202e37ec5',
    current_timestamp_milliseconds=current_timestamp_milliseconds,
    app_key=Configuration.appKey,
    ep_data=ep_data
)
params = {
    "jsv": "2.7.4",
    "appKey": Configuration.appKey,
    "t": current_timestamp_milliseconds,
    "sign": sign,
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "timeout": "10000",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp32",
    "data": ep_data,
}
headers = {
    'cookie': cookie,
    'referer': 'https://s.taobao.com/search',
    'user-agent': ua,
}
response = requests.get(url, params=params, headers=headers)
response_data = json.loads(re.search('\{.*\}', response.text).group())['data']

print(response_data)
