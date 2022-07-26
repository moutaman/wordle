from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import base64


caps = {}
caps["appium:udid"] = "5do7bu95ukkfaqbi"
caps["platformName"] = "android"
caps["appium:appPackage"] = "com.vottzapps.wordle"
caps["appium:appActivity"] = "com.unity3d.player.UnityPlayerActivity"
caps["appium:noReset"] = True
caps["appium:fullReset"] = False
caps["appium:autoGrantPermissions"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

classic = "546,915"

keyboard = {
    "A":"111,1577",
    "B":"575,1737",
    "C":"370,1",
    "D":"328,1605",
    "E":"265,1454",
    "F":"437,1605",
    "G":"546,1605",
    "H":"656,1609",
    "I":"815,1450",
    "J":"765,1605",
    "K":"874,1605",
    "L":"983,1605",
    "M":"803,1773",
    "N":"698,1773",
    "O":"933,1450",
    "P":"1038,1450",
    "Q":"59,1450",
    "R":"387,1450",
    "S":"223,1605",
    "T":"496,1450",
    "U":"710,1450",
    "V":"487,1773",
    "W":"172,1450",
    "X":"273,1773",
    "Y":"609,1450",
    "Z":"168,1773",
}


def choose_game():
    time.sleep(20)
    TouchAction(driver).tap(x=546, y=915).perform()
    print("choosing game")
    time.sleep(2)


def map_keyboard(key):
    x,y = keyboard[key].split(",")
    return x,y

def send_keys(word):
    time.sleep(2)
    print("sending keys: " + word)
    for key in word:
        x,y = map_keyboard(key)
        TouchAction(driver).tap(x=int(x), y=int(y)).perform()
        time.sleep(0.5)
    time.sleep(1)
    TouchAction(driver).tap(x=525, y=1929).perform()

def get_screen_shot():
    time.sleep(5)
    screenshotBase64 = driver.get_screenshot_as_base64()
    print(screenshotBase64)
    with open("im.png", "wb") as im:
        im.write(base64.b64decode((screenshotBase64)))

choose_game()
time.sleep(10)
send_keys("ABOUT")
get_screen_shot()


