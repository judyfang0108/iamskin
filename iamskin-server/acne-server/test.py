import requests
import json
import pyimgur


def upload_img_to_imgur(client_id, imgpath):
    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(imgpath, title="Uploaded with PyImgur")
    return upload_image.link


def get_acne_result(url, format):
    r = requests.post(
        "http://192.168.2.102:8080/acne-classifier/",  # 此網址須根據server調整
        data=json.dumps({
            'image': url, 'format': format}),
        timeout=(2, 15),
        headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})

    response = r.json()
    return response


def acne(data, format):
    result = get_acne_result(data, format)
    return result.get('count'), result.get('prediction')


if __name__ == "__main__":
    link = upload_img_to_imgur('efffb8956702928', "levle0_0.jpg")
    count, ans = acne(link, 'url')
    print(ans)
