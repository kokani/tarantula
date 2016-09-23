© Amit Sawant, Sept 2016

# tarantula
Read clinic information

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

COMMENT(S)
----------

-Results of the test run are in tarantula\groupon_dental_clinics.txt
-This can be done without using Selenium and using HTTP requests, which will be faster. But with Selenium
offers couple of benefits which HTTP requests don't,
1. This crawler will also work for sites which build html content on the page by running Javascript.
2. Debugging is easier, since you can see the page loaded in a browser, when the crawler crashes its easier to
determine the cause.
-To crawl more sites to need to add a new folder in the sites folder and customize the three files in the
groupon folder for the site


