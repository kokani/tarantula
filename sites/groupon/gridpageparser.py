# coding=utf-8
# © Amit Sawant, Sept 2016

import sys
import traceback

from bs4 import BeautifulSoup

from tarantula.sites.parent_grid_page_parser import ParentGridPageParser
from tarantula.clinic_bo import ClinicBO

#Parses the grid page which has all dental clinics
class GridPageParser(ParentGridPageParser):

    def parse(self, pageHtml):
        clinicBOs = set()
        cntClinicTags = 0
        soup = BeautifulSoup(pageHtml, "html.parser", from_encoding='utf-8')
        divTag = soup.find('div', id='pull-cards', recursive=True)
        if divTag:
            clinicTags = divTag.find_all('figure', recursive=False)
        else:
            return idToClinicBOs
        
        for clinicTag in clinicTags:
            try:
                #Url
                aTag = clinicTag.find('a', recursive=True)
                url = aTag["href"]
                #Name
                divTag = clinicTag.find('div', class_="cui-merchant-name", recursive=True)
                name = divTag.text.strip()
                
                clinicBO = ClinicBO(name, url)
                clinicBOs.add(clinicBO)
            except:
                excepMessage = traceback.format_exc(sys.exc_info())
                print excepMessage
                continue
        
        return clinicBOs

if __name__ == "__main__":
    f = open("clinics.html", 'r')
    pageHtml = f.read()
    f.close()
    
    parser = GridPageParser()
    clinicBOs = parser.parse(pageHtml)
    for clinicBO in clinicBOs:
        print "---------------------------"
        print clinicBO
        