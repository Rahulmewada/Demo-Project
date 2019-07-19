from  selenium import webdriver  # open web driver
from selenium.webdriver.common.keys import Keys  # use for key value
import time   # time for time sleep
import re    # regular expression for mach the word
from pymongo import MongoClient  # use for server
import datetime      # use date and time
from geotext import GeoText   # nlp used for remove place and city name



# Data store in Mongodb

# def mdb_server(res,src):   # res = image caption and src = image link
#     conn = MongoClient('mongodb://localhost:27017')
#     db = conn['InstaBoot']
#     cName = db['dataIn']
#     mydata = {}
#     mydata['caption']=res
#
#
#
#
#     filter_name = re.findall(r'@\w+\S+\w',res) # @ pattern check
#
#
#     hashtag = re.findall(r'#\w+\S+\w',res) # hashtag pattern check
#     print(hashtag)



    # # c = cName.insert_one({'#hashtag':hashtag})
    # # print(c)
    #
    # date_time = datetime.datetime.now()
    #
    #
    # a = cName.insert_many([{'details_caption':res,'@name': filter_name,'#hashtag':hashtag,"image_url":src,"status":"False",'date':date_time}])
    # print(a)
    #




class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome(r'C:\Users\User\Downloads\chromedriver.exe') # chrome driver path

    def CloseBrowser(self):
        self.driver.close()

    def LogIN(self):
        driver = self.driver

        # web page url
        try:
            driver.get('https://www.instagram.com/')
            time.sleep(2)
        except Exception as e:
            print("Error in opening url",e)
            pass

            # click on login button
        try:
            login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
            login_button.click()
            time.sleep(3)
        except Exception as e:
            print("Error in clicking on log in",e)
            pass

               # user id or name
        try:
            user_name = driver.find_element_by_name('username')
            user_name.clear()
            user_name.send_keys(self.username)
            time.sleep(4)
        except Exception as e:
            print("Error in writing username",e)
            pass

        # user password
        try:
            user_pass = driver.find_element_by_name('password')
            user_pass.clear()
            user_pass.send_keys(self.password)
            user_pass.send_keys(Keys.RETURN)
            time.sleep(3)
        except Exception as e:
            print("Error in wriring password",e)
            pass

                        # rempove apps pop
        try:
            app_pop = driver.find_element_by_xpath('//*[@id="react-root"]/div/div[2]/a[2]')
            app_pop.click()
            time.sleep(2)
        except Exception as e:
            print("Error in clicking pop up",e)
            pass



                            # remove pop
        try:
            pop_cl = driver.find_element_by_xpath('/ html / body / div[3] / div / div / div[3] / button[2]')
            if pop_cl:
                pop_cl.click()
                time.sleep(3)
        except Exception as e:
            print("Error in clikcing on another pop up if available",e)
            pass



                                # profile page
        try:
            profile_id = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(3) > a > span')
            profile_id.click()
            time.sleep(5)
        except Exception as e :
            print("Error in clicking on profile id",e)
            pass

            # search page name
        try:
            # page_name = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            # page_name.clear()
            # time.sleep(5)

            driver.get('https://www.instagram.com/indorizayka/')
            time.sleep(3)
        except Exception as e:
            print("Error in opening url of page",e)
            pass


    def ImageClick(self):
        driver = self.driver
        try:
            clic_pic = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')

            clic_pic.click()
            time.sleep(5)
        except Exception as e:
            print("error image clicking",e)
            pass
        try:
            a=InstagramBot.Comment()
            print("in comment")
        except:
            pass





    def Comment(self):
        driver = self.driver
        for r in range(1,5):

            try:
                time.sleep(3)
                res=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div[2]/span').text   # caption xpath (take span)

                # remove city name

                res1 = res.replace('#', ' ')
                sp = res1.split()
                ls = []
                for i in sp:
                    c = i.capitalize()
                    a1 = GeoText(c)
                    # city_name=[]
                    # city_name.append(a.cities)
                    # str1 = str(city_name)
                    ls.append(a1.cities)
                print(ls)

                while ([] in ls):
                    ls.remove([])
                print("fhfh", ls)
                # for r in range(0,len(ls)+1):
                #     sp.remove(ls[r][0])
                #     print('sp list', sp)


                # remove ads image

                list1 = ['promotion', 'ads', 'booking','hiring','job','ElectionSpecial','Election']

                s1 = set(res.split())
                s2 = set(list1)
                a = s1.intersection(s2)
                print(a)



                try:
                    time.sleep(3)
                    # img_path = driver.find_element_by_xpath(
                    #     '/html/body/div[3]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img')
                    img_path=driver.find_element_by_class_name("FFVAD")
                    img_src = img_path.get_attribute('src')
                    print('src : ', img_src)

                    try:
                        if a:
                            print('in a ')
                            pass
                        else:
                            mdb_server(res,img_src)
                            time.sleep(3)
                            print('mongodb server ')
                            pass
                        # print(i)

                        try:
                            if r == 1:
                                scroll = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()  # click next buttun xpath
                                print("scroll ",r)
                                print('click button ')
                            else:
                                time.sleep(3)
                                driver.find_element_by_xpath(
                                    "/html/body/div[3]/div[1]/div/div/a[2]").click()  # click second button xpath
                                print('second button ',i)
                                time.sleep(1)
                        except Exception as e:
                            print("error in clicking next:", e)
                            pass


                    except Exception as e:
                        print("Error in getting url of image:", e)
                        pass


                except Exception as e:
                    print("Error  or image src:", e)
                    pass

            except Exception as e:
                print("Error in reading caption:", e)
                pass





        # var = res.find_element_by_tag_name('a')
        # for i in range(1,20):
        #      res=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div[2]/span/a['+str(i)+']').text
        #      caption=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li/div/div/div[2]/span/br['+str(i)+']').text
        #      print(res)
        #      print(caption)

    # def download_img(self):
    #     driver = self.driver
    #     img_path = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img')
    #
    #     #a = img_path.find_elements_by_link_text('src')
    #     c = img_path.get_attribute('src')
    #
    #    # print('image : ',a)
    #     print('src : ', c)



def search():
    conn = MongoClient('mongodb://localhost:27017')
    db = conn['InstaBoot']
    cName = db['dataIn']

    res=cName.find({"status":"False"}).limit(2)
    var=list(res)
    print(var)
    return var



def follow():
    a=InstagramBot('foodi_indore','food@2000')
    a.LogIN()
    following={}
    db=MongoClient().InstaBoot
    collect=db["following_candidate"]
    try:
        # click follower xpath
        a.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
        for r in range(1, 25):
            time.sleep(2)
            try:
                # match following requested x path
                check=a.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button').text

                if check=="Requested":
                    pass
                else:
                    a.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[' + str(r) + ']/div/div[2]/button').click()

                    following['name']=a.driver.find_element_by_xpath('//*[@id="f2909ce785a8a58"]/div/div/a').text
                    #following["date"]=datetime.date.now()
                    #collect.insert_one(following)


                    date_mdb = db.following_candidate.insert_one({"date": datetime.datetime.now()})
                    print(date_mdb)

                    following["no"] = r
            except Exception as e:
                print("Error in clicking on follow",e)
                pass
    except Exception as e:
        print("Error in clicking on followers",e)







id_pass = InstagramBot('foodi_indore','food@2000')
id_pass.LogIN()
id_pass.ImageClick()
id_pass.Comment()


search()
follow()

#id_pass.download_img()


