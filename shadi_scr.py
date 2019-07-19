from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from bs4 import BeautifulSoup
import re

def data_base(a):
    conn = MongoClient('mongodb://localhost:27017')
    db = conn['lovevivah']
    c_Name = db['s_data']
    #my_data = {}
   # my_data['caption'] = name,age,gender,hight,drink,img_src
    print('mongodb server')

    b = c_Name.insert_one(a)
    print('mongodb data :',b)

class ShadiData():

    def __init__(self,username, password):
        self.username = username
        self.password = password

        self.driver =  webdriver.Chrome(r'C:\Users\User\Downloads\chromedriver.exe')

    def CloseBrowser(self):
        self.driver.close()

    def Data(self):
        driver = self.driver

        driver.get('https://www.lovevivah.com/login_controller/login')
        # window_before = driver.window_handles[0] # switch function use for second window
        # print('window before : ',window_before)

        try:
             # log in id
            user_name = driver.find_element_by_id('emailid')
            user_name.clear()
            user_name.send_keys(self.username)
            time.sleep(2)

        except Exception as e:
            print('erron on log in id name : ',e)
            pass



        try:
            # log in pass
            user_pass = driver.find_element_by_id('password')
            user_pass.clear()
            user_pass.send_keys(self.password)
            time.sleep(1)

        except Exception as e:
            print('erron on log in password : ', e)
            pass

        try:

            driver.find_element_by_xpath('//*[@id="LoginBTN"]').click() # login click

        except Exception as e:
            print('erron on login click : ', e)
            pass
        try:

            driver.find_element_by_xpath('//*[@id="navbar"]/ul/li[4]/a').click() #  click on discover maches

        except Exception as e:
            print('erron on discover match : ', e)
            pass

    def page_url(self):
        driver = self.driver

        page_src = driver.page_source
        print(page_src)


        url_list = []
        d = {}

        regex_fun = re.compile(r'="https://www.lovevivah.com/userprofile_controller/view_profile/557263.*?"')
        out = re.findall(regex_fun,page_src)
        #print(out)
        url_list = [i.strip('"') for i in out]
        for i in (url_list):
            driver.get(i)
            print('driver url : ',driver.current_url)
            time.sleep(2)
            try:
                driver.back()
                d['name'] = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[2]').text # name xpath
                #print('name : ',name)
                time.sleep(2)
            except Exception as e:
                print('error in name x path ')

            try :

                d["age"] = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[10]').text # age xpath
                #print('age : ',age)
                time.sleep(2)

            except Exception as e:
                print('error in age x path ')

            try:

                d['gender'] = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[12]').text # gender xpath
                #print('Gender',gender)
                time.sleep(2)

            except Exception as e:
                print('error in gender x path ')

            try:

                d['hight'] = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[14]').text # hight xpath
                #print('hight : ',hight)
                time.sleep(2)

            except Exception as e:
                print('error in hight x path ')

            try:

                d['drink'] = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/ul/li[6]').text
                #print('drink : ',drink)
                time.sleep(2)

            except Exception as e:
                print('error in drink xpath ')

            try:

                src_in = driver.find_element_by_xpath('//*[@id="section-basic"]/div[2]/div/div/div/div[1]/div/img')
                d['img_src'] = src_in.get_attribute('src')
                #print('img_src : ',img_src)
                time.sleep(3)
            except Exception as e:
                print('error in image src x path ')
            print('Dictionary data : ',d)
            data_base(d)
            #data_base(name, age, gender, hight, drink, img_src)

obj1 = ShadiData('rj.netliz@gmail.com','rahul@2000')
obj1.Data()
obj1.page_url()
data_base()