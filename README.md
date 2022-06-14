# Mission-to-Mars
The objective of this project is to automate a web browser to visit different websites to extract data about the Mission to Mars. The scraped data is stored in the NoSQL database, MongoDB and then is rendered in a web application created with Flask. 

![image](https://user-images.githubusercontent.com/103223944/173466510-078008b9-4c11-413a-aa0b-8cb17b43400f.png)

## Web Scraping
BeautifulSoup and Splinter are used to automate a web browser and perform the web scrape. The scraping.py file is developed to extract data from the Mars NASA news website, a Mars featured image from the spaceimages-mars.com and full-resolution mars hemisphere images from the marshemispheres.com.

## MongoDB
A MongoDB database is created to store the data from the web scrape.

## Web Application
A web application is developed using Flask to display the data from the web scrape. The App.py file is developed to connect to the MongoDB, extract the stored scrape data and render the HTML file. Bootstrap components are used to polish and customize the HTML page.

## Results
The web application includes different information about the Mars. The user can click on the "Scrape New Data" to update the conetent based on the latest data from the original webpages.  



![image](https://user-images.githubusercontent.com/103223944/173467485-e93fad3a-831c-4d06-a2bc-21d586ceb3c2.png)
