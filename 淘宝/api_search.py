'''
淘宝搜索接口
逆向sign参数
'''


import requests
import json
import urllib.parse
from tools import Tools
from js_reverse.sign import sign
from config import token, cookie, UA
import time


appKey = "12574478"
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
null = None

querystring_data_params = json.dumps({
    "device":"HMA-AL00","isBeta":"false", "grayHair":"false","from":"nt_history","brand":"HUAWEI","info":"wifi","index":"4",
    "rainbow":"","schemaType":"auction","elderHome":"false","isEnterSrpSearch":"true","newSearch":"false","network":"wifi",
    "subtype":"","hasPreposeFilter":"false","prepositionVersion":"v2","client_os":"Android","gpsEnabled":"false",
    "searchDoorFrom":"srp","debug_rerankNewOpenCard":"false","homePageVersion":"v7","searchElderHomeOpen":"false",
    "search_action":"initiative","sugg":"_4_1","sversion":"13.6","style":"list","ttid":"600000@taobao_pc_10.7.0",
    "needTabs":"true","areaCode":"CN","vm":"nw","countryNum":"156","m":"pc","page":2,"n":48,"q":urllib.parse.quote('茶具的'),
    "qSource":"manual","pageSource":"a21bo.jianhua/a.search_manual.0","channelSrp":"","tab":"all","pageSize":"48",
    "totalPage":"100","totalResults":"217952","sourceS":"1","sort":"_coefp","bcoffset":"-3","ntoffset":"0","filterTag":"",
    "service":"","prop":"","loc":"","start_price":null,"end_price":null,"startPrice":null,"endPrice":null,"categoryp":"",
    "ha3Kvpairs":null,"myCNA":"0z/PGhe3ByUCAXd7KbNtZt3e","screenResolution":"1680x1050","viewResolution":"1680x4162",
    "userAgent":UA,
    "couponUnikey":"","subTabId":"","np":"","clientType":"h5","isNewDomainAb":"false","forceOldDomain":"false"
}, separators=(',', ':'))

querystring_data = json.dumps({
    "appId":"34385",
    "params":querystring_data_params,
}, separators=(',', ':'))

querystring = {
    "api":"mtop.relationrecommend.wirelessrecommend.recommend",
    "v":"2.0","timeout":"10000","type":"jsonp","dataType":"jsonp",
    "callback":"mtopjsonp47",
    "data":querystring_data,
    # "bx-ua":"234!caheKS1ieePWok8jOA/NuadwzIAqwKzkWPV1mcGLuiqGP6OkVolqOsqVm0DLwG2mHtJV7lW2Z1i3526JCHcY7RhFh5DKdzK+YWKKrS31Agkhe7xONVcd0ut//T4vsPJcVck5hDnuFGPATSc/fNtc7vm5rpde0fMdqwsywY1eebnkZ3oHQQVNC24uepWH9iHjg4Lgz3kOc4olZZodQQymhsWZn3TH9iJXPkE7A3s/clV7Z3oHQQx1L5iOZ3Td9iJTCPcZQpk8c247nZodQCyNhsfeZ3wTdiyKCPsZQkkic247DZ0GQCyDlsfWepDTH1dTCP5+/ks/c24HjZodQCyDPMf5ef+TMAJ7hLZZQks/cs5TZZoHQCVmh2tZn3pRVYyQ7loZQppvcs4TZY4GknwFnMtZhpwd57dTJvUZQkp/cskce3DTQihmtM/KVuVH9Ad7hpoZQksvGdV7jtQ4PFXB/f5ua4+W9Ad7hIZZQ3U0YLttZ32sUQXmBssZn3UH9AH1AMUNOARsoNvDA4HUePkbWoOnaPa2S3lAEjE2WaCc+jvbEPYBB3SSEiebPevqAZvak0vQWSSutFrDaVUvyvk740uXPdHTXflA5iDAaemcmq5jgbQ4dBki40MIfLv5a8ZnFc1OA4zVQkH1mBaXBjk17jSrD4Gv1nhpPu0tLNnZn+W31eoA7QzWdOb/OaX1aBu5ZlxZpk6Jrzdnk39S+TWd6IHwbrOTme1gVM1uXP5wj0AAKrkq4s7dhmqERPXEErlRo/aOnvWtgvVg+Ot5qFimlSfrBf67dXj6CtNRUM9EcPNtydS36G83QhlW9lzQxuFVsmQQX+cgYTKQ/+QUyP9nnZn2MV9usr8qP+b+1g/y6TvhHM+fqLaYfNR06c0HEPHvWTQJSMONYNFhY+iudJXjqTdPmvoc/o5WfmhOZhM8JoWeSLV/Aj8Qbd5oCOh3SjbtjlsUkX4+uuoVEP+nDEobG2rwiJIq2w8JY/uO3GbLw8HnPhaciVmtmSva+yDQloKkz8ag9g0Kp0en6J2g9qjGFewGcM2SYx/nvUCnnPMPC16/D94UDcKinYrWoL95g+DafbXRtAEzxpCYCAbylhdMjtZuJXCIH9TFodmPZw5KD15paJu/KdRobLKflGcLOQo7j1r9ryCG7DGFG50VxamcFXRmWRVjk69sLmoC/Vnke4xDrXr+THEWGwf29Z1uY7Jd5030tB0b7bblcjjKJFYB66nC2jvyDVVNLlkckVMIGr0pivvnDV3QAF5nhEt6DqwFlR//tVxeGya/8LpYZ6KHmkk5q6IgYJvlAchFdYipoBgDkeeeqTIiX1eNExaccDuLombEtgJ1DwQPljpsfU7zwyGIW6IQnO64GsTg+tNALVNtVn5f2+Whf4ZAFnGyFFaYSLLDn9r+P/WXHPnxOoRuGHKHTtEysU1Gcm3t7r7dqcTmfQYI0qFf08bRbfuvUoZwm3uYJeDSxVrxw0c4JOMCqKZ/Tj9ZponcMoXbewmxiTgaTN6JWn0OYvrLxPyEBNCPYhJ/fSrGRQjLcm/3IqJd9V9B4C1LbPxQ6kXfyb09gILMazX8CLr+OxjJQ8XDll2CroQzjdfJesPxcvsRNZkVjp9Q44rt9S4koGE5+hE7if5ThRNBLgDjFtm+VJprZzrPvzS6EXeoJ+g2nyH3EsiXqf3W2jh6pfSWy9WCNbSTUtiAHazDRi9yGLWDe9LM5zjC3xIHiWewK+HBIFWcO9OOr+Gegkdji4zRwR9jdle2RFFhPvnzETEIJCoZY0dMvfNTBx27d2cy0QhHJvNbMolCMhYPm3R727/odyBw+gHHmleOA3wmegxVW7xvJa2DOJWQPrljYDKWrq1GWxbFFGoYHS48OaJdJhMaLpzNEMyHXWLK7xY33ZWhfj7IkPNJLNL4zeiGUGy1iddhZhxT14a+1H6iGauh2060S9xslj0kWRuAx9yHVLr5xm24QbBcQU0bjRpEdju1SAOurGhnj0EHXfEk/7A+FMNom2nLnKow094QupwoAUPk1/ajoFKNaVEF",
    # "bx-umidtoken":"T2gAuUdUJkAYMgT0Et802ipM88xlEk3U5wT2oBYwtXwGBSiOaXQrH2SE72qxy401qLE=",
    # "bx_et":"h8nEsrNOMMBJOFZKN2Rm1SL6NkEL2yh5V7Z7ZFVg6MauNehzzbGTrDZIdfPoGbySA0TspvLtGSyxY7qGsAe7Z7fefkp32uAXGNsuJnlEolY8Zuvaj825-uV3t1vaU-PuqW4lsN20s7quqbqgI8yPr7V3q1jg68quZbVhSdy7sJquqbDMQ8d16gu_kFW1nQRMNVJ7LyPlVlkrhLwr1SknYXlnbiUEjG17p8Eo-vGal2RVY2knkbemt6AUQDkq4qcMfMrrIqmzjHJ5MgSSGs-yFBDKtql9YstxRWkZof7ePhmE92giNHIkaQigolrwmNmEvfhtLbxwG39xyjg_otLX-Lg7X431rOKxmvnbljyaQYzc8xOBz3LPyaUggRPXpWQRyym4QS9wQaQ8JFeaGpFd."
}

timestamp = str(int(time.time()*1000))
sign = sign(token, timestamp, appKey, querystring["data"])
print(sign)
querystring.update({
    'jsv':'2.7.4',
    'appKey':appKey,
    't': timestamp,
    'sign':sign,
})


payload = ""
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "referer": "https://s.taobao.com/search?clientPreloadId=preload_1783932181912&commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E8%8F%8A%E8%8A%B1&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.search_manual.0&ssid=s5-e&tab=all",

    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": UA,
    "Cookie": cookie,
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)


response_data = Tools.jsonp(response.text, querystring['callback'])
print(response_data)
