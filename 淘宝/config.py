import re

# 可以自行修改
cookie = ""
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/527.36"



token = re.search(r"_m_h5_tk=(.*?)_", cookie).group(1)
