
# Import Splinter and BeautifulSoup
from posixpath import defpath
from pandas.core.frame import DataFrame
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    
    # headless=False :we could see the scraping in action, True: run broweser in headless mode so we do not see it
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True) 

    news_title, news_paragraph = mars_news(browser)   

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    # searching for elements with a specific combination of tag (div) and attribute (list_text)
    # as an example, ul.item_list would be found in HTML as <ul class="item_list">.
    # wait one second before searching for components.
    
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #CSS works from right to left, such as returning the last item on the list instead of the first.
    #tehrfore for select_one: the first matching element returned will be a <li /> element with a class 
    # of list_test and all nested elements within it.
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:

        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
    
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title,news_p


def featured_image(browser):
    
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try: 
        # Find the relative image url
        # .get('src') pulls the link to the image
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

def mars_facts():

    try:
        # returns a list of tables found in the HTML
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())