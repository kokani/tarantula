
from selenium import webdriver
from optparse import OptionParser
import importlib


def run(options):
	siteName = options.siteToCrawl.lower()

	#Grid page parser
	gridParser = importlib.import_module("tarantula.sites" + siteName + ".gridpageparser.GridPageParser")
	gridParser = getattr(gridParser, parts[-1])

	#Site's config
	confModule = importlib.import_module("tarantula.sites" + siteName + ".lclconf")

	clinicBOS = set()
	for url in confModule.urls:
		#Launch the page in selenium
		driver = webdriver.Chrome()
        driver.set_page_load_timeout(100)
        driver.maximize_window()

        driver.get(url)



def readClinics():


if __name__ == "__main__":
	parser = OptionParser()
    parser.add_option("-s", "--siteToCrawl", help="Site to crawl.")
    (options, args) = parser.parse_args()

	run(options)