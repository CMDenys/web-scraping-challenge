from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests

import os

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def scrape_info():


    # def init_browser(): ----------------------------------------------------------
    # Open ChromeDriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
        # browser= init_browser()

    #First step, visit the mars.nasa.gov.news website.
    news_url = "https://mars.nasa.gov/news/"
    time.sleep(3)
    browser.visit(news_url)

    mars_data = {}

    #html object -----------------------------------------------------------------
    html = browser.html
    soup = bs(html, 'html.parser')
    #scrape the most recent title  -----------------------------------------------
    start = soup.find('li', class_="slide")
    title = start.find('div', class_='content_title').text.strip()

    #scrape the most recent teaser paragraph -------------------------------------
    news_start = soup.find("li", class_= "slide")
    news_p = news_start.find('div', class_="article_teaser_body").text
        
    mars_data["title"] = title
    mars_data["news_p"] = news_p
        
    #Featured image jpl ----------------------------------------------------------
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)
    time.sleep(1)
    browser.find_link_by_partial_text('FULL IMAGE').click()
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
    images = soup.find_all('div', class_='floating_text_area')

    for image in images:
        link = image.find("a")
        href = link['href']
        
        featured_image_url = ("https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + href)

        mars_data["featured_image_url"] = featured_image_url

    #Fact Tables ------------------------------------------------------------------
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_table_df = tables[0]
    mars_tableII = mars_table_df.set_index(0, inplace=True)
    mars_tableIII = mars_table_df.rename(columns={0:' ',1:' '})
    mars_html_table = mars_tableIII.to_html()
    mars_html_table_clean = mars_html_table.replace("\n", "")
    mars_html_table_clean
    mars_data['mars_html_table_clean'] = mars_html_table_clean

    #Hemispheres -------------------------------------------------------------------

    # Setup splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemi_url)

    jpg_list=browser.find_by_css("a.product-item h3")

    mars_hemi_image_urls = []

    for x in range(len(jpg_list)):
        hemi={}
        browser.find_by_css("a.product-item h3")[x].click()
        sample = browser.links.find_by_text("Sample").first
        hemi["img_url"]=sample["href"]
        hemi["title"]=browser.find_by_css("h2.title").text
        mars_hemi_image_urls.append(hemi)
        browser.back()

    mars_hemi_image_urls    
    mars_data["hemi"]=mars_hemi_image_urls 


    browser.quit()

    return mars_data

if __name__ == "__main__":
    print(scrape_info())