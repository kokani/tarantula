# coding=utf-8
# © Amit Sawant, Sept 2016

def GetVisibleElement(driver, selector):
    elements = driver.find_elements_by_xpath(selector)
    for ele in elements:
        if ele.is_displayed():
            return ele

    return None



