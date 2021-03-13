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
    # data_dict{}

    #First step, visit the mars.nasa.gov.news website.
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, "html.parser")
    #scrape the first headline and paragraph
    news_title = soup.find_all('div', class_="content_title")[0].text.strip()
    news_p = soup.find_all("div", class_= "rollover_description_inner")[0].text.strip()

    #Second step, visit the JP
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, "html.parser")
    #scrape the featured image
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
    
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    html = browser.html
    soup = bs(html, "html.parser")
    tables = pd.read_html(facts_url)
    mars_table_df = tables[0]
    mars_table_df.columns = ["Description", "Fact"]
    html_table = mars_table_df.to_html()
    html_table.replace('\n', '')

