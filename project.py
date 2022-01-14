from selenium import webdriver
from bs4 import BeautifulSoup
import time , csv
START_URL='https://en.m.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser=webdriver.Chrome('chromedriver_win32/chromedriver.exe')
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers=['v_mag','proper_name','bayer_designation','distance','spectral_class','mass','radius','luminosity']
    star_data=[]
    for i in range(0,50):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for th_tag in soup.find_all('th',attrs={'class','wikitable sortable'}):
            tr_tags=th_tag.find_all('tr')
            temp_list=[]
            for index,tr_tag in enumerate(tr_tags):
                if index==0:
                    temp_list.append(tr_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append('')
            star_data.append(temp_list)
    with open('project.csv','w') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)
scrape()