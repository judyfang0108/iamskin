import requests
import json


def get_acne_result(url, format):
    r = requests.post(
        " http://192.168.2.102:8080/acne-classifier/",
        data=json.dumps({
            'image': url, 'format': format}),
        timeout=(2, 15),
        headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})

    response = r.json()
    return response


def acne(data, format):
    result = get_acne_result(data, format)
    return result.get('count'), result.get('prediction')


# call server方法
predicted_count, ans = acne('image_path', 'url')  # image_path放imgur網址

# 根據結果對應圖片
if ans == 'Mild':  # low

elif ans == 'Moderate':  # middle

elif ans == 'Severe':  # m_high

else:  # high
