
class ClinicBO:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        
        self.address = None
        self.tel = None
        self.description = None
        
    def __str__(self):
        return "Name: {0}\nUrl: {1}".format(self.name, self.url)
        # return "Name: {0}\nTel: {1}\nAddress: {2}\nUrl: {3}".format(self.name, self.tel, self.address, self.url)
