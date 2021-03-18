<h1 style="color:blue"> web-scraping-challenge </h1>


Step 1 - Scraping

Initital scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and used it to complete all scraping and analysis tasks. The following outlines what was scraped.

<u>NASA Mars News</u>
- The first scrape is from the Nasa Mars site and consisted of the both the latest News Title and Paragraph Text.

JPL Mars Space Images - Featured Image
- The second srape is of the JPL Featured Space Image.  Splinter was used to navigate the site and find the image url for the current Featured Mars Image.  Once found, the image url string was assigned a variable called featured_image_url.

Mars Facts
- The third scrape is from the Mars Facts webpage here and is a table of relevant facts.  Pandas was used to scrape the table containing facts about the planet and data was then converted to an HTML table string.
- 
Mars Hemispheres


Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.


You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.


Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.


Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.



