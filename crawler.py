# coding=utf-8
# © Amit Sawant, Sept 2016

import sys
import time

from selenium import webdriver
from optparse import OptionParser
import importlib

from tarantula.sites.groupon.gridpageparser import GridPageParser
from tarantula.sites.groupon.clinicpageparser import ClinicPageParser
from tarantula import Utils

class Crawler:

    def __init__(self):
        self.gridPageDriver = None
        self.clinicPageDriver = None
        self.confModule = None

    def run(self, options):
        siteName = options.siteToCrawl.lower()

        #Site's config
        self.confModule = importlib.import_module("tarantula.sites." + siteName + ".lclconf")
        
        clinicBOS = set()
        for url in self.confModule.urls:
            #Launch the page in selenium
            self.gridPageDriver = webdriver.Chrome()
            self.gridPageDriver.set_page_load_timeout(100)
            self.gridPageDriver.maximize_window()

            self.gridPageDriver.get(url)
            
            #Close the pop up
            self.confModule.on_grid_page_load(self.gridPageDriver)
            
            clinicBOS.update(self._readClinics(siteName))
        
        #Persist to file
        f = open("groupon_dental_clinics.txt", "w")
        idx = 1
        for clinicBO in clinicBOS:
            f.write(str(idx) + ". ")
            f.write(str(clinicBO))
            f.write("\n")
            idx = idx + 1
        f.close()

    def _readClinics(self, siteName):
        allReadClinicBOs = set()
        
        #Grid page parser
        gridParser = GridPageParser()
        
        #Read first page
        pageHtml = self.gridPageDriver.page_source.encode('utf-8')
        clinicBOs = gridParser.parse(pageHtml)
        
        #Load clinic page for each clinic
        #Initialize the driver
        self.clinicPageDriver = webdriver.Chrome()
        self.clinicPageDriver.set_page_load_timeout(100)
        self.clinicPageDriver.maximize_window()
        allReadClinicBOs = self._readClinicPages(clinicBOs)
        
        #Check if more pages exist
        pageNo = 2
        firstPageUrl = self.gridPageDriver.current_url
        newUrl = firstPageUrl + "&page=" + str(pageNo)
        while (True):
            self.gridPageDriver.get(newUrl)
            pageHtml = self.gridPageDriver.page_source.encode('utf-8')
            clinicBOs = gridParser.parse(pageHtml)
            if not clinicBOs:
                break
            #Load clinic page for each clinic
            readClinicBOs = self._readClinicPages(clinicBOs)
            currCnt = len(allReadClinicBOs)
            print "Total clinics read until now: " + str(currCnt)
            allReadClinicBOs.update(readClinicBOs)
            newCnt = len(allReadClinicBOs)
            print "Total clinics read after this page: " + str(newCnt)
            if currCnt == newCnt:
                #No more pages
                break
            pageNo = pageNo + 1
            newUrl = firstPageUrl + "&page=" + str(pageNo)
        
        return allReadClinicBOs
        
    def _readClinicPages(self, clinicBOs):
        clinicPageParser = ClinicPageParser()
        readClinicBOs = set()
        for clinicBO in clinicBOs:
            #Add some delay, not to bombard the site
            time.sleep(1)
            self.clinicPageDriver.get(clinicBO.url)
            #Close the pop up
            self.confModule.on_grid_page_load(self.gridPageDriver)
            
            pageHtml = self.clinicPageDriver.page_source.encode('utf-8')
            wasParsedSuccessfully = clinicPageParser.parsePageAndSetBO(pageHtml, clinicBO)
            if wasParsedSuccessfully:
                readClinicBOs.add(clinicBO)
            else:
                print "\nNot a clinic, skipping: " + clinicBO.name
            
        return readClinicBOs

    def __del__(self):
        #Close browsers
        if self.gridPageDriver:
            self.gridPageDriver.quit()
        if self.clinicPageDriver:
            self.clinicPageDriver.quit()
    

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--siteToCrawl", help="Site to crawl.")
    (options, args) = parser.parse_args()
    if options.siteToCrawl is None:
        parser.error("Site to crawl needs to be specified.")

    crawler = Crawler()
    crawler.run(options)
    