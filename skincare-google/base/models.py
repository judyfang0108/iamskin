import matplotlib.pyplot as plt
from django.db import models
import base64
from PIL import Image
import io
import matplotlib
import requests
import json
# import pyimgur

matplotlib.use('Agg')

# Create your models here.
# load pretrained DenseNet and go straight to evaluation mode for inference
# load as global variable here, to avoid expe
# load pretrained DenseNet and go straight to evaluation mode for inference
# load as global variable here, to avoid expensive reloads with each request


def plot_pie(likelihood):
    labels = []  # 製作圓餅圖的類別標籤
    size = []  # 製作圓餅圖的數值來源
    for key in likelihood.keys():
        labels.append(key)
        size.append(likelihood.get(key))

    separeted = [0, 0, 0]  # 依據類別數量，分別設定要突出的區塊
    max_val = size.index(max(size))
    separeted[max_val] = 0.1

    colors = ['tomato', 'lightskyblue', 'goldenrod']  # 圓餅圖顏色

    plt.figure(figsize=(9, 6))  # 顯示圖框架大小
    plt.pie(size,  # 數值
            labels=labels,  # 標籤
            autopct="%1.1f%%",  # 將數值百分比並留到小數點一位
            explode=separeted,  # 突出的區塊
            pctdistance=0.6,  # 數字距圓心的距離
            colors=colors,  # 顏色
            textprops={"fontsize": 12},  # 文字大小
            shadow=True,
            )  # 設定陰影
    plt.axis('equal')  # 使圓餅圖比例相等
    plt.title("Pie chart of skin type", {"fontsize": 18})  # 設定標題及其文字大小
    plt.legend(loc="best")  # 設定圖例及其位置為最佳

    buffer = io.BytesIO()
    plt.savefig(buffer,  # 儲存圖檔
                bbox_inches='tight',  # 去除座標軸占用的空間
                pad_inches=0.0)  # 去除所有白邊

    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)  # 对plot_data进行编码
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    return imd
    # plt.savefig("Pie chart of skin type.jpg",  # 儲存圖檔
    #             bbox_inches='tight',  # 去除座標軸占用的空間
    #             pad_inches=0.0)  # 去除所有白邊
    # plt.close()      # 關閉圖表


def decode(code=None):
    code = str.encode(code)
    code = base64.b64decode(code)
    code = io.BytesIO(code)
    image = Image.open(code)
    return(image)


def get_skin_result(url, format):
    r = requests.post(
        "https://skin-test.herokuapp.com/skin-classifier/",  # 膚質server位置
        data=json.dumps({
            'image': url, 'format': format}),
        timeout=(2, 15),
        headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})

    response = r.json()
    return response


def skin(data, format):
    result = get_skin_result(data, format)
    return result.get('likelihood'), result.get('prediction')


def get_nail_result(url, format):
    r = requests.post(
        "https://nail-test.herokuapp.com/nail-classifier/",  # 指甲server位置
        data=json.dumps({
            'image': url, 'format': format}),
        timeout=(2, 15),
        headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})

    response = r.json()
    return response


def nail(data, format):
    result = get_nail_result(data, format)
    return result.get('likelihood'), result.get('prediction')


def get_acne_result(url, format):
    r = requests.post(
        "http://35.185.146.67:5000/acne-classifier",  # 痘痘server位置
        data=json.dumps({
            'image': url, 'format': format}),
        timeout=(2, 15),
        headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})

    response = r.json()
    return response


def acne(data, format):
    result = get_acne_result(data, format)
    return result.get('count'), result.get('prediction')
