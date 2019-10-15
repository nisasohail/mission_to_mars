# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Mission-to-Mars'))
	print(os.getcwd())
except:
	pass

#%%
# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pymongo
import time
import pandas as pd
from requests import RequestException
from selenium import webdriver


#%%
#Scrape page
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


#%%
#Define url and browse the site using chrome.
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


#%%
# save the most recent article, title and date
article = soup.find("div", class_="list_text")
news_paragraph = article.find("div", class_="article_teaser_body").text
news_title = article.find("div", class_="content_title").text
news_date = article.find("div", class_="list_date").text
print(news_date)
print(news_title)
print(news_paragraph)


#%%
#Title
news_title = soup.find('div',class_='content_title').text
news_title


#%%
#article
news_p = soup.find('div', class_='article_teaser_body').text
news_p


#%%
image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url_featured)


#%%
# HTML Object
html_image = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_image, 'html.parser')
# Retrieve background-image url from style tag
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
# Website Url
main_url = 'https://www.jpl.nasa.gov'
# Concatenate website url with scrapped route
featured_image_url = main_url + featured_image_url
# Display full link to featured image
featured_image_url 


#%%
#Mars weather twitter url page https://twitter.com/marswxreport?lang=en
url_3 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url_3)
html_3 = browser.html
tweet_soup = BeautifulSoup(html_3, 'html.parser')


#%%
#Save the tweet text for the weather report as a variable called mars_weather.
mars_weather = tweet_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_weather


#%%
# Visit Mars facts url
facts_url = 'http://space-facts.com/mars/'
table = pd.read_html(facts_url)
table[0]


#%%
# Visit hemispheres website through splinter module
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)


#%%
# HTML Object
html_hemispheres = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_hemispheres, 'html.parser')
# Retreive all items that contain mars hemispheres information
items = soup.find_all('div', class_='item')
# Create empty list for hemisphere urls
hemisphere_image_urls = []
# Store the main_ul
hemispheres_main_url = 'https://astrogeology.usgs.gov'
# Loop through the items previously stored
for i in items:
   # Store title
   title = i.find('h3').text
   # Store link that leads to full image website
   partial_img_url = i.find('a', class_='itemLink product-item')['href']
   # Visit the link that contains the full image website
   browser.visit(hemispheres_main_url + partial_img_url)
   # HTML Object of individual hemisphere information website
   partial_img_html = browser.html
   # Parse HTML with Beautiful Soup for every individual hemisphere information website
   soup = BeautifulSoup( partial_img_html, 'html.parser')
   # Retrieve full image source
   img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
   # Append the retreived information into a list of dictionaries
   hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
# Display hemisphere_image_urls
hemisphere_image_urls


#%%



