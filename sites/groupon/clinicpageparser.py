# coding=utf-8
# © Amit Sawant, Sept 2016
	
from bs4 import BeautifulSoup
    
from tarantula.sites.parent_clinic_page_parser import ParentClinicPageParser

#Parses each clinics page
class ClinicPageParser:

    def parsePageAndSetBO(self, pageHtml, clinicBO):
        soup = BeautifulSoup(pageHtml, "html.parser", from_encoding='utf-8')
        divTag = soup.find('div', class_='address icon-marker-filled', recursive=True)
        if not divTag:
            return False
        pTags = divTag.find_all('p', recursive=True)
        address = []
        tel = None
        for pTag in pTags:
            if pTag.text and pTag.text.strip():
                txt = pTag.text.strip()
                if txt.startswith("+") or txt.isdigit():
                    #tel
                    tel = txt.strip("+")
                else:
                    #Address
                    address.append(txt)

        clinicBO.address = address
        clinicBO.tel = tel
        
        return True
    
from selenium import webdriver
    
def test(clinicUrl):
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(100)
    driver.maximize_window()
    driver.get(clinicUrl)
    
    cpp = ClinicPageParser()
    html = driver.page_source.encode('utf-8')
    cpp.parse(html, None)
    
    driver.close()
    
if __name__ == "__main__":
    test("https://www.groupon.com/deals/west-end-dental-associates-1")
    