from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time


# def init_browser():
   


def scrape():
    
 # Open ChromeDriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # browser= init_browser()

    #First step, visit the mars.nasa.gov.news website.
    news_url = "https://mars.nasa.gov/news/"
    time.sleep(3)
    browser.visit(news_url)

    mars_data = {}

    #html object
    html = browser.html
    soup = bs(html, 'html.parser')
    #scrape the most recent title
    start = soup.find('li', class_="slide")
    title = start.find('div', class_='content_title').text.strip()

    #scrape the most recent teaser paragraph
    news_start = soup.find("li", class_= "slide")
    news_p = news_start.find('div', class_="article_teaser_body").text

    print(title)
    print(news_p)
    
    mars_data["title"] = title
    mars_data["news_p"] = news_p
    
    #Second step, visit  JPL
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

#     #Fact Tables
#     facts_url = 'https://space-facts.com/mars/'
#     tables = pd.read_html(facts_url)
#     mars_table_df = tables[0]
#     mars_table_df.rename(columns={"0": "Mars Planet Profile", "1" : "Facts"}, inplace=True)
#     html_table = mars_table_df.to_html()
#     html_table.replace('\n', '')
#     mars_table.to_html('table.html')

#     #Hemispheres
#     hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#     # Setup splinter
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

#     browser.visit(hemi_url)
#     html = browser.html
#     soup = bs(html, 'html.parser')

#     hemi_main_url = "https://astrogeology.usgs.gov"
#     full_url_dict = []

#     hemi_names = soup.find_all('div', class_='item')

#     for i in hemi_names:
#         title_hemi = i.find("h3").text.strip()
#         link = i.find('a')['href']
#         enhanced_img_link = hemi_main_url + link
#         #move to page with full picture
#         browser.visit(enhanced_img_link)
#         html = browser.html
#         soup = bs(html, 'html.parser')
#         enhanced_img = soup.find("div", class_="downloads")
#         final_link = enhanced_img.find('a')['href']
    
    
#     full_image_url_link = (hemi_main_url + final_link)
# #     print(title)
# #     print(full_image_url_link)
    
#     full_url_dict.append({
#         "Hemisphere Image" : title_hemi, 
#         "URL" : final_link
  

  
#     mars_data
#     mars_data["full_url_dict"] = full_url_dict
 

    browser.quit()  
    return mars_data




    

