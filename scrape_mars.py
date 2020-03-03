#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


#  # Step 1 - Scraping
#  # NASA Mars News

# In[2]:


# Scrape the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
base_URL = "https://mars.nasa.gov/news"
JPL_URL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
JPL_URL2 = "https://www.jpl.nasa.gov"

driver = webdriver.Firefox()
driver.get(base_URL)
html_text = driver.page_source

soup = BeautifulSoup(html_text, "html.parser")

latest_title = soup.find("div", class_="content_title").text
print(f"The latest Title: {latest_title}")

latest_paragraph = soup.find("div", class_="article_teaser_body")
print(f"The latest paragraph: {latest_paragraph}")


# ### JPL Mars Space Images - Featured Image

# In[3]:


r = requests.get(JPL_URL)
html = r.text
soup = BeautifulSoup(html, "html.parser")


# In[4]:


mars_images_path = soup.find("footer").a
mars_images_path


# In[5]:


all_mars_image_url = JPL_URL2 + mars_images_path["data-fancybox-href"]
all_mars_image_url


# ### Mars Weather

# In[6]:


# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page.
# Save the tweet text for the weather report as a variable called mars_weather.


# In[7]:


mars_weather_url = "https://twitter.com/marswxreport?lang=en"
html_text = requests.get(mars_weather_url).text
soup = BeautifulSoup(html_text, "html.parser")
mars_weather = soup.find(
    "p", "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"
).text
mars_weather


# ### Mars Facts

# In[8]:


Mars_Facts_URL = "https://space-facts.com/mars/"
Mars_Facts_df = pd.read_html(Mars_Facts_URL)[0]
Mars_Facts_df.columns = ["Mars Facts", "Values/Units"]
Mars_Facts_df.set_index("Mars Facts")


# ### Mars Hemispheres

# In[9]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


# In[10]:


Mars_Hemispehers_URL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
driver.get(Mars_Hemispehers_URL)
html_text = driver.page_source
soup = BeautifulSoup(html_text, "html.parser")
all_names_hemispeher = soup.find_all("h3")
for all_name in [name.text for name in all_names_hemispeher]:
    print(all_name)


# In[11]:


all_picture_path = [e.a["href"] for e in soup.find_all("div", "description")]
all_picture_path
for path in all_picture_path:
    print(path)


# In[12]:


whole_image_link = []
URL_a = "https://astrogeology.usgs.gov"
[
    whole_image_link.append(URL_a + all_picture_path[i])
    for i in range(len(all_picture_path))
]
i = 0
for link in whole_image_link:
    print(f"{[name.text for name in all_names_hemispeher][i]}:{link}")
    i += 1


# In[13]:


image_url = []
for i in range(len(whole_image_link)):
    driver.get(whole_image_link[i])
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "html.parser")

    image_url.append(URL_a + soup.find_all("img", class_="wide-image")[0]["src"])
image_url


# In[14]:


Hemisphere_image_url = []
for i in range(len(image_url)):
    hemi_dict = {}
    hemi_dict["title"] = all_names_hemispeher[i].text
    hemi_dict["url"] = image_url[i]
    Hemisphere_image_url.append(hemi_dict)
Hemisphere_image_url

print("=======================================================")

def scrape():
    mars_data = {
        "Latest_News_Title": latest_title,
        "Latest_Paragraph": latest_paragraph,
        " Featured_Image": all_mars_image_url,
        " Mars_Weather": mars_weather,
        "Mars_Facts": Mars_Facts_df,
        "Hemisphares_Pages": image_url,
    }
    return(mars_data)




# In[15]:


# it is done finally...
