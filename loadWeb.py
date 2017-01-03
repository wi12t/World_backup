import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url_id = 76
url = "http://12tails.herorangers.com/newsupdate/news?cate=2&content="
counter = 0
while url_id < 811:
    req = requests.get(url+str(url_id))
    print(".",end='')
    counter += 1
    if req.text.find("ไม่พบข้อมูลค่ะ") < 0:
        print(counter)
        times = time.time()
        print("\tSnapshot Content "+str(url_id).zfill(3)+ " tarting")
        service_args = [
            '--ignore-ssl-errors=true',
            '--cookies-file=test.cookies',
            '--disk-cache=true'
            ]
        driver = webdriver.PhantomJS(service_args=service_args)
        driver.set_window_size(1366, 768) # set the window size that you need
        driver.get(url+str(url_id))
        driver.save_screenshot('news/12t_'+str(url_id).zfill(3)+'.png')
        print("\tSnapshot Content "+str(url_id)+" Finished! @"+str(round(time.time()-times,3)))
        counter = 0
    url_id += 1