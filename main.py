from selenium.webdriver.common.keys import Keys
from torcontrol import renew_ip,start_tor
from firefoxcontrol import get_driver
from random import randrange
import time

url="https://www.youtube.com/watch?v=FgvPIWBQ4Sc"

start_tor()
time.sleep(5)

while 1:
    driver=get_driver()
    driver.get(url)
    butonkabul=driver.find_elements_by_xpath("//span[contains(text(), 'Kabul ediyorum')]/ancestor::button")
    if(butonkabul):
        butonkabul[0].click()
    try:
        video = driver.find_element_by_id('movie_player')
    except:
        video=0
    if(video):
        video.send_keys(Keys.SPACE) #hits space
        for i in range(randrange(20,40)):
            video.send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
            butonreklam=driver.find_elements_by_xpath("//span[contains(text(), 'Reklamları Atla')]/ancestor::button")
            if(butonreklam):
                butonreklam[0].click()
                i=0
    driver.quit()
    renew_ip()
    
