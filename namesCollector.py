import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import *

def write_sorted_list_to_file(file_path, my_list):
    sorted_list = sorted(my_list)
    with open(file_path, 'w') as f:
        for title, link in sorted_list:
            f.write("%s ==> %s\n" % (title, link))

def load_sorted_list_from_file(file_path):
    with open(file_path, 'r') as f:
        return [(line.split(" ==> ")[0], line.split(" ==> ")[1]) for line in f]


def login(dr, user, mp , provider):
    dr.get(provider)
    time.sleep(1)
    dr.find_element(By.CLASS_NAME, "user-login").click()
    time.sleep(1)
    dr.find_element(By.NAME, "username").send_keys(user)
    dr.find_element(By.NAME, "password").send_keys(mp)
    time.sleep(1)
    captchar = input("Enter captchar: ")
    print(captchar)
    time.sleep(2)
    dr.find_element(By.NAME, "captchar").send_keys(captchar)
    time.sleep(1)
    dr.find_element(By.ID, "submit_login").click()
    time.sleep(5)


def bookmark(dr):
    time.sleep(2)
    dr.get(PROVIDER+'bookmark')
    time.sleep(2)
    PAGELINK = "https://manganato.com/bookmark?page="

    max = dr.find_element(By.CLASS_NAME,"go-p-end").get_attribute('href')
    lastPage = max.split("=")[1]
    lastPage = int(lastPage)
    print("last  page value = " + str(lastPage))
    parent_div = dr.find_element(By.CLASS_NAME, "user-bookmark-content")
    childs_div = parent_div.find_elements(By.CLASS_NAME, "user-bookmark-item")
    count = len(childs_div)
    print(count)
    titlesLink = []
    time.sleep(1)
    for div in childs_div:
       title = div.find_element(By.CLASS_NAME, "bm-title")
       link = title.find_element(By.TAG_NAME, "a")
       titlesLink.append((title.text, link.get_attribute('href')))
    
    for i in range(2, lastPage+1):
        dr.get(PAGELINK+str(i))
        time.sleep(2)
        parent_div = dr.find_element(By.CLASS_NAME, "user-bookmark-content")
        childs_div = parent_div.find_elements(By.CLASS_NAME, "user-bookmark-item")
        for div in childs_div:
            title = div.find_element(By.CLASS_NAME, "bm-title")
            link = title.find_element(By.TAG_NAME, "a")
            titlesLink.append((title.text, link.get_attribute('href')))

    return titlesLink
    

def get_names_link():
    driver = webdriver.Chrome()
    login(driver, user, mp, PROVIDER)

    titles = bookmark(driver)
    print("printing titles and links: ")
    for title, link in titles:
        print(title + "  ==>  " + link)
    write_sorted_list_to_file(MANGAFILE, titles)

    driver.quit()



if __name__ == "__main__":
    manga = load_sorted_list_from_file(MANGAFILE)
    for title, link in manga:
        print(title + "  ==>  " + link)