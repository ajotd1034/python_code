from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import time


if __name__ == '__main__':

    # appium setting    
    appium_server_url = 'http://localhost:4723/wd/hub'

    options = AppiumOptions()

    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '11')
    options.set_capability('deviceName', 'Samesung')
    options.set_capability('appPackage', 'com.android.chrome')
    options.set_capability('appActivity', 'com.google.android.apps.chrome.Main')

    # create webdriver
    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(60)
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]

    # google帳號未登入狀態下，要進行的處理
    el_dismiss = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (AppiumBy.ID, 'com.android.chrome:id/signin_fre_dismiss_button')))
    el_dismiss.click()

    el_located = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (AppiumBy.ID, 'com.android.chrome:id/ack_button')))
    el_located.click()

    # 開啟網頁
    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    # 確保網頁已完全開啟並截圖
    time.sleep(10)
    driver.get_screenshot_as_file('./main_page.png')

    # 點擊左上角選單
    el_main = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (AppiumBy.XPATH, "(//android.view.View[@content-desc=\"  \"])[1]/android.widget.TextView")))
    el_main.click()

    # 點擊產品介紹
    xpath_product = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
        android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/\
            android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/\
                android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/\
                    android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/\
                        android.view.View[1]/android.view.View/android.view.View[1]/\
                            android.view.View/android.widget.TextView"
    el_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (AppiumBy.XPATH, xpath_product)))
    el_product.click()

    # 點擊信用卡列表
    xpath_credit_card = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
        android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/\
            android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/\
                android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/\
                    android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/\
                        android.view.View[1]/android.view.View/android.view.View[1]/\
                            android.view.View[2]/android.view.View/android.view.View[1]/\
                                android.view.View/android.widget.TextView"
    el_credit_card = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (AppiumBy.XPATH, xpath_credit_card)))
    el_credit_card.click()

    # 確保網頁已完全開啟並截圖
    time.sleep(5)
    driver.get_screenshot_as_file('./credit_card_list_page.png')

    # 點擊卡片介紹
    xpath_credit_card_intro = "(//android.view.View[@content-desc=\"卡片介紹\"])[1]/\
        android.widget.TextView"
    el_credit_card_intro = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (AppiumBy.XPATH, xpath_credit_card_intro)))
    el_credit_card_intro.click()

    # 確保網頁已完全開啟
    time.sleep(5)

    # 滑動畫面至停發卡片位置並截圖
    x1 = width * 0.5
    y1 = height * 0.70   
    y2 = height * 0.25

    for i in range(9):
        driver.swipe(x1, y1, x1, y2, 1000)
        # time.sleep(2)

    x1 = width * 0.75
    x2 = width * 0.25
    y1 = height * 0.5

    for i in range(13):
        driver.get_screenshot_as_file(f'./discontinued_credit_card_{i + 1}.png')
        driver.swipe(x1, y1, x2, y1, 500)
        time.sleep(1)

    driver.quit()
