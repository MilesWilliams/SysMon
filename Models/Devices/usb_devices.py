class USBDevice (object):
    def __init__(self, iManufacturer, idVendor, idProduct, bcdUSB=None):
        self.iManufacturer = iManufacturer
        self.idVendor = idVendor
        self.idProduct = idProduct
        self.bcdUSB = bcdUSB
