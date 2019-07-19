from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from utilities import *


from bs4 import BeautifulSoup
from pymongo import MongoClient
import time
import re
import config
import urllib.parse as urlparse
from urllib.parse import urlencode
from bson import ObjectId

def get_url_id(url):
    try:
        uid = re.findall("\d+", url)[0]
        return uid
    except Exception as e:
        print("Exception in finding id from url : ",e)
        return ObjectId()


def data_base( name,age,gender,hight,drink,img_src):
    conn = MongoClient('mongodb://localhost:27017')
    db = conn['shadi']
    c_Name = db['s_data']
    my_data = {}
    my_data['caption'] = name,age,gender,hight,drink,img_src
    print('mongodb server')

    a = c_Name.insert_many([{'name':name,'age':age,'gender':gender,'hight':hight,'drink':drink,'image':img_src}])
    print('data input in mongodb : ',a)


def do_login(driver,email_id,password):
    "Function to Do Login in Love Vivah Portal"

    try:
        driver.get('https://www.lovevivah.com/login_controller/login')
        driver.find_element_by_id('emailid').send_keys(email_id)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_xpath('//*[@id="LoginBTN"]').click() # login click
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click() #  click on discover maches
        return driver
    except Exception as e:
        print('Exception in Login Function : ', e)
        pass
    return driver


def get_page_urls(driver,scroll_cnt):
    "Function to get profile urls from a page to scroll count"
    output_urls=[]
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(0, scroll_cnt):
        page_source = driver.page_source
        regex_fun = re.compile(r'https://www.lovevivah.com/userprofile_controller/view_profile/?\d+\?.*?"')
        out = re.findall(regex_fun, page_source)
        url_list = list(set([i.strip('"') for i in out]))
        print("url_list : ", len(url_list))
        # Appending new urls to old one
        [output_urls.append(i) for i in url_list if i not in output_urls]
        random_sleep()

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     break
        # last_height = new_height
        scroll_page(driver=driver)

    return output_urls


def get_profile_data(url,driver):
    driver.get(url)
    print('current url : ',driver.current_url)
    outdict = {}
    outdict["_id"] = get_url_id(url=url)
    outdict["name"] = ""
    outdict["age"] = ""
    outdict["gender"] = ""
    outdict["height"] = ""
    outdict["image_urls"] = []

    try:
        name = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[2]').text # name xpath
        outdict["name"] = name
    except Exception as e:
        print("Exception in finding Name Details : ",e)
        pass

    try:
        age = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[10]').text # age xpath
        outdict["age"] = age
    except Exception as e:
        print("Exception in finding Age Details : ",e)
        pass

    try:
        gender = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[12]').text # gender xpath
        outdict["gender"] = gender
    except Exception as e:
        print("Exception in finding Gender Details : ",e)
        pass

    try:
        hight = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[14]').text # hight xpath
        outdict["height"] = hight
    except Exception as e:
        print("Exception in finding Height Details : ",e)
        pass

    try:
        src_in = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/div/div/div/div[1]/div/img')
        img_src = src_in.get_attribute('src')
        outdict["image_urls"].append(img_src)
    except Exception as e:
        print('Exception in finding Image Details : ',e)
        pass

    print("profile_data : ",outdict)
    return outdict


if __name__ == '__main__':
    db = MongoClient('mongodb://localhost:27017')['face-detection-dataset']['lovevivah.com']
    email_id = 'rj.mewada480@gmail.com'
    pass_wd = 'pari@2000'
    chrome_options = options.Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(config.chrome_path, chrome_options=chrome_options)
    driver.maximize_window()

    driver = do_login(driver,email_id,pass_wd)
    from pprint import pprint
    profile_urls = get_page_urls(driver=driver, scroll_cnt=50)
    pprint(profile_urls)

    for url in profile_urls:
        profile_data = get_profile_data(url,driver)
        profile_data["weight"]=""
        profile_data["source"]="lovevivah.com"
        save_to_db(db, profile_data)