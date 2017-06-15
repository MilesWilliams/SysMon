import usb.core
import usb.backend.libusb1
from Models.Devices.usb_devices import USBDevice


class USBController(object):

    def __init__(self):
        self.busses = usb.busses()

    def get_all_devices(self):
        deviceList = []
        deviceList.clear()
        for bus in self.busses:
            devices = bus.devices
            for dev in devices:
                print(dev)
                if dev != None:
                    try:
                        xdev = usb.core.find(idVendor=dev.idVendor, idProduct=dev.idProduct)
                        usbType = ""
                        if xdev._manufacturer is None:
                            xdev._manufacturer = usb.util.get_string(xdev, xdev.iManufacturer)
                        if xdev._product is None:
                            xdev._product = usb.util.get_string(xdev, xdev.iProduct)
                        if hex(xdev.bcdUSB) != None:
                            hexVal = str(hex(xdev.bcdUSB))
                            version = hexVal[2:3]
                            subVersion = hexVal[3:4]
                            usbType = "USB " + str(version) + "." + subVersion
                        print(xdev._manufacturer)
                        if xdev._manufacturer != 'Apple Inc.':

                            if xdev._manufacturer is None:
                                deviceList.clear()
                                print("no")
                                return False
                            elif xdev._manufacturer is not None:
                                deviceList.append(USBDevice(xdev._manufacturer, xdev._product, dev.idVendor, usbType))
                                print('sending')
                                return deviceList

                    except:
                        pass
        return deviceList
