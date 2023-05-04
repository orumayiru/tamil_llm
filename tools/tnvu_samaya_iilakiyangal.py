#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 06:20:26 2023

@author: aki
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 06:22:02 2023

@author: aki
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
from tqdm import tqdm
link = 'https://www.tamilvu.org/slet/l4110/l4110uri.jsp?song_no={}&book_id=109&head_id=59&sub_id=1538'
link_ls = []
for i in tqdm(range(1,1470)):
    link_ls.append(link.format(i))
count = 1
for j in link_ls:
    # Create a new instance of the Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Create a new instance of the Chrome driver with the headless option
    driver = webdriver.Chrome(options=chrome_options)
    # Navigate to the web page
    driver.get(j)
    # Find all the text in the page using the "body" tag
    all_text = driver.find_element(By.CSS_SELECTOR, "body").text.split("\n")
    # Find all the text in the "poem" class
    poem_text = driver.find_element(By.CSS_SELECTOR, ".poem").text.split("\n")
    # Find all the text in the "link" class
    link_text = driver.find_element(By.CSS_SELECTOR, ".link").text.split("\n")
    # Print the results
    venba = ' '.join(poem_text)
    urai = ' '
    for line in all_text:
        if line not in poem_text:
            if line not in link_text:            
                urai = urai + ' ' + line
    mydict = {}
    mydict["meta"]=[{"venba_no":count}]
    count+=1
    mydict["venba"] = venba.strip()
    mydict["urai"] = urai.strip()
    with open('devaram_onram_thrumurai.json', "a",encoding='utf-8') as f:
        json.dump(mydict, f, ensure_ascii=False,indent=4)
        f.write(',')
        f.write('\n')
    driver.quit()
