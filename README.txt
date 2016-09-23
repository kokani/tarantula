© Amit Sawant, Sept 2016

# tarantula
Read clinic information

COMMENTS
--------

-Results of my test run are also in the folder in the file groupon_dental_clinics.txt. Some records on 
those pages are not actual clinics but deals of products, which have been skipped so the count on the 
dental category of 263 is incorrect, the real count is close to whats in the results file.
-This can be done without using Selenium and using HTTP requests, which will be faster. But with Selenium
offers couple of benefits which HTTP requests don't,
1. This crawler will also work for sites which build html content on the page by running Javascript.
2. Debugging is easier, since you can see the page loaded in a browser, when the crawler crashes its easier to
determine the cause.
-To crawl more sites to need to add a new folder in the sites folder and customize the three files in the
groupon folder for the site

LIBRARIES
---------

python2.7, Selenium, BeautifulSoup4, chrome browser

SETTINGS
--------

Set PYTHONPATH,

PYTHONPATH=....PARENT_FOLDER\tarantula

HOW TO RUN
----------

1. cd to tarantula folder
2. Run this command,

python crawler.py -s groupon


