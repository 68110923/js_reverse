import hashlib


def sign(token, timestamp, api_key, params) -> str:
    string = f'{token}&{timestamp}&{api_key}&{params}'
    return hashlib.md5(string.encode()).hexdigest()



if __name__ == '__main__':
    print(sign('sdfsdgdf', '26456343546', '23456', '{}'))
