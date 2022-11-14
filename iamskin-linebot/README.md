# iamskin-Linebot

## 介紹
精準醫療的關鍵在於預防，愛美膚旨在透過AI人工智慧與醫療的跨域結合，提供創新且方便使用的醫療服務，從被動接受治療到主動預防疾病，以加強民眾之自主健康管理。

## 資料夾介紹
* linebot: 存放linebot的code
    * flexMessage: 存放用Flex Message Simulator製作的flexMessage的json檔
* linebot_menu: 存放圖文選單的code


## Locally 執行方法
You can using `ngrok` as a proxy.

### Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**Connect your account**
```sh
cd /path/to/ngrok.zip

./ngrok authtoken 'your authtoken'
```


**`ngrok` would be used in the following instruction**

```sh
./ngrok http 8000
```

After that, `ngrok` would generate a https URL.

Open Line Developers page and set Webhook to 'URL'/callback 

### Run the sever

```sh
python3 app.py
```

### 將url貼至line Developers的Webhook URL
![](https://i.imgur.com/R9P0WrY.png)
