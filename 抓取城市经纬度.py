import time
import requests
import pandas as pd
from geopy.geocoders import Nominatim

posi = pd.read_excel(r"D:\工作文件\21日.xlsx")
address = posi["城市"].tolist()
num = posi["文章数"].tolist()
print(num)
def getid(dizhi):
    addinfo = []
    j=0
    for i in dizhi:
        try:
            # 利用百度地图api查询，每天有2000条的限制
            # addinfo.append(baiduApi(i, num[j]))
            # 利用nominatimApi 查询
            addinfo.append(nominatimApi(i, num[j]))
            j = j + 1
        except:
            print("地址{}获取失败，请稍后重试！".format(i))
            time.sleep(.5)
    print("所有地址均已获取完毕！！！")
    print(addinfo)
    f = open(r'D:\工作文件\21日.txt','w')
    f.write(addinfo)
    return addinfo

def baiduApi(city, num):
    url = "http://api.map.baidu.com/geocoder/v2/"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    payload = {
        'output': 'json',
        'ak': 'X8zlxPUdSe2weshrZ1WqnWxb43cfBI2N'
    }
    info = {}
    content = requests.get(url, params=payload, headers=header).json()
    print(content)
    info['lon'] = content['result']['location']['lng']
    info['lat'] = content['result']['location']['lat']
    info['city'] = city
    info['num'] = num
    print("当前查询城市信息：" + str(info))
    return info

def nominatimApi(city, num):
    info = {}
    gps = Nominatim()
    location = gps.geocode(city)
    info['lon'] = location.longitude
    info['lat'] = location.latitude
    info['city'] = city
    info['num'] = num
    print ("当前查询城市信息：" + str(info))
    return info

if __name__ == "__main__":
 #计时开始：
    t0 = time.time()
    myaddress = getid(address)
    t1 = time.time()
    total = t1 - t0
    print("消耗时间：{}".format(total))