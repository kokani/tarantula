	
from bs4 import BeautifulSoup
    
from tarantula.sites.parent_clinic_page_parser import ParentClinicPageParser

class ClinicPageParser:

    def parse(self, pageHtml, clinicBO):
        soup = BeautifulSoup(pageHtml, "html.parser", from_encoding='utf-8')
        divTag = soup.find('div', class_='address icon-marker-filled', recursive=True)
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

        print address, tel
        clinicBO.address = address
        clinicBO.tel = tel
    
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
    