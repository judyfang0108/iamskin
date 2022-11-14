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

* **Linebot 官方開發網站/工具:**
    * Line Developers: 建立/管理linebot帳號
    https://developers.line.biz/console/channel/1656975873
    * Line Official Account Manager: 
    https://account.line.biz/login?redirectUri=https%3A%2F%2Fmanager.line.biz%2Faccount%2F%40627kkxpf%2Frichmenu%2F5592773
    * Linebot Python SDK:
    https://github.com/line/line-bot-sdk-python
    * Flex Message Simulater:
    https://developers.line.biz/console/register?redirect=%2Fflex-simulator%2F
* **Linebot教學:**
    * 基礎教學1:
    https://ithelp.ithome.com.tw/articles/10229943
    * 基礎教學2:
    https://kanido386.github.io/2021/07/fsm-line-bot/
    * 基礎教學3:
    https://kanido386.github.io/2021/07/hackathon-line-hint/
    * flex message:
    https://ithelp.ithome.com.tw/articles/10223020
    * 圖文選單:
    https://medium.com/enjoy-life-enjoy-coding/%E4%BD%BF%E7%94%A8-python-%E7%82%BA-line-bot-%E5%BB%BA%E7%AB%8B%E7%8D%A8%E4%B8%80%E7%84%A1%E4%BA%8C%E7%9A%84%E5%9C%96%E6%96%87%E9%81%B8%E5%96%AE-rich-menus-7a5f7f40bd1
* **圖片處理工具**:
    * 圖片儲存: https://imgur.com/
    * GIF製作: https://gifmaker.me/
    * 製作手機模擬圖: https://qurb.rishimohan.me/
* **注意事項**
    * line 官方帳號的權限之後再給你
    * 可以先使用ngork在local端測試(記得去Line Developers網站改網址)
    * 佈署時記得將dotenv的地方註解掉
    * 佈署的時候記得把app.py最下面的app.run的debug模式設為False 
* **可以改進之處**
    * database建立(目前只簡單的用python list來存user狀態，之後可以考慮加入database提升穩定性，以應付更多使用者)
