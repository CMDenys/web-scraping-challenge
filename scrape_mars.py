from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import pymongo

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

@app
def scrape():
    browser = init_browser()

    mars_data = {}

    #First step, visit the mars.nasa.gov.news website.
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    #scrape the most recent title
    start = soup.find('li', class_="slide")
    title = start.find('div', class_='content_title').text.strip()
    title

    #scrape the most recent teaser paragraph
    news_p = soup.find_all("div", class_= "article_teaser_body")[0].text.strip()
    news_p

    #Second step, visit  JPL
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
    images = soup.find_all('div', class_='floating_text_area')

    for image in images:
        link = image.find("a")
        href = link['href']
        
        print("https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/" + href)
        
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
        
    #Fact Tables
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_table_df = tables[0]
    mars_table_df.rename(columns={"0": "Mars Planet Profile", "1" : "Facts"}, inplace=True)
    html_table = mars_table_df.to_html()
    html_table.replace('\n', '')
    mars_table.to_html('table.html')

    #Hemispheres
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(hemi_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    hemi_main_url = "https://astrogeology.usgs.gov"
    full_url_dict = []

    hemi_names = soup.find_all('div', class_='item')

    for i in hemi_names:
        title = i.find("h3").text.strip()
        link = i.find('a')['href']
        enhanced_img_link = hemi_main_url + link
        #move to page with full picture
        browser.visit(enhanced_img_link)
        html = browser.html
        soup = bs(html, 'html.parser')
        enhanced_img = soup.find("div", class_="downloads")
        final_link = enhanced_img.find('a')['href']

    
        full_url_dict.append({
            "Hemisphere Image" : title, 
            "URL" : final_link
        })
    
full_url_dict

mars_data['title'] = title
mars_data['news_p'] = news_p
mars_data['featured_image_url'] = featured_image_url
mars_data['full_url_dict'] = full_url_dict




    

