
import sys

from bs4 import BeautifulSoup

from tarantula.sites.parent_grid_page_parser import ParentGridPageParser
from tarantula.clinic_bo import ClinicBO

class GridPageParser(ParentGridPageParser):

	def parse(self, pageHtml):
		clinicBOs = set()
	    cntClinicTags = 0
	    soup = BeautifulSoup(pageHtml, "html.parser", from_encoding='utf-8')
	    divTag = soup.find('div', id='pull-cards', recursive=True)
	    if divTag:
	        clinicTags = divTag.find_all('figure', recursive=False)
	        self.cntClinicTags = self.cntClinicTags + len(productTags)
	        cntProdTags = len(clinicTags)
	    else:
	        return idToClinicBOs
	    
	    for clinicTag in clinicTags:
	        try:
	            #Url
	            url = self.getClinicUrl(clinicTag, self.homeUrl)
	            #Name
	            divTag = clinicTag.find('div', class_="cui-merchant-name", recursive=True)
	            name = divTag.text.strip()

	            clinicBO = ClinicBO(name, url)
	            clinicBOs.add(clinicBO)
	        except:
	            self.handleGriPageException(sys.exc_info(), clinicTag, "GroupOn")
	            continue
	    
	    return clinicBOs
