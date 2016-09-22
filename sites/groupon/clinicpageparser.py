	
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
					tel = text.strip("+")
				else:
					#Address
					address.append(txt)

		clinicBO.address = address
		clinicBO.tel = tel

	