import folium
import time
import requests
from urllib.request import quote
import numpy as np
import pandas as pd
import seaborn as sns
import webbrowser
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

def makeHeatMap():
    posi = []
    result = []
    for i in posi:
        info = [i['lat'], i['lon'], float(i['num'] / 1000)]
        result.append(info)
    map_osm = folium.Map(location=[35, 110], zoom_start=5)  # 绘制Map，开始缩放程度是5倍
    HeatMap(result).add_to(map_osm)  # 将热力图添加到前面建立的map里
    file_path = r"D:\workSpace\python\地图test.html"
    map_osm.save(file_path)  # 保存为html文件
    webbrowser.open(file_path)  # 默认浏览器打开