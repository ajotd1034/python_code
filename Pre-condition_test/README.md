### ex_1~3：40分鐘

### Appium & Selenium：10小時

* 測試環境：
  * 手機：Samesung A22
  * Android version：11
  * Chrome app version：116.0.5845.172

* 安裝套件與解決問題：1小時
  * 套件
    * npm：9.6.7
    * Node.js：18.17.1
    * Android studio：2022.3.1
    * Appium desktop：1.15.1
    * Appium commandline：2.1.3
    * Appium-docker：1.16.2
    * java-sdk：20
    * java-jre：8
    * Python (3.8，原先已安裝)
      * Appium-Python-Client：3.0.0
      * Selenium：4.12.0
  * 解決安裝時遇到的問題：30分鐘
    * Node.js版本，導致appium安裝失敗
    * 最新版本的jdk不提供jre

設計測試流程：9小時

1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。
3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖

測試結果(未登入Google的情況下必須先點擊01和02兩張圖上黃框的按鈕)

* 第1步已完成
  * 有遇到的問題的部分在於我使用的Selenium和Appium都是最新版本，界面都有大幅更動，在找資料時，大部分都是舊的寫法
* 第2步只有完成到信用卡列表並截圖的部分
  * 對於元素架構的組成不是很熟悉，大部分的時間都是花在如何從父節點下取得子節點的數量，但還是無法取得
* 第3步也是只有完成滑動到指定位置，並依序截圖的部分
  * 遇到的問題同2.，也是對元素架構的組成不是很清楚，無法正確的取得需要的資訊，原本預期作法是要持續滑動到有"本卡已停止申辦"的部分，就停止，截圖然後向右繼續滑動，一樣確認是否有關鍵字，依序截圖，直到無法滑動為止
