# coding=utf-8
# © Amit Sawant, Sept 2016

class ClinicBO:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        
        self.address = None
        self.tel = None
        self.description = None
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
      return other and self.name == other.name
        
    def __str__(self):
        return "Name: {0}\nTel: {1}\nAddress: {2}\nUrl: {3}".format(self.name, self.tel, self.address, self.url)
