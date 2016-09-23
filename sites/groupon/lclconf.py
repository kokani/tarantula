# coding=utf-8
# © Amit Sawant, Sept 2016

from tarantula import Utils

homeurl="https://www.groupon.com"

urls = ["https://www.groupon.com/browse/new-york?category=health-and-fitness&category2=dental"]

def on_grid_page_load(driver):
    #Close the pop up
    noThanks = Utils.GetVisibleElement(driver, "//a[contains(text(), 'No Thanks')]")
    if noThanks:
        noThanks.click()
        print "Closed the popup"
