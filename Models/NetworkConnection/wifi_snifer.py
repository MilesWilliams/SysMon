import objc
from .wifi_model import WifiModel

objc.loadBundle('CoreWLAN',
                bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                module_globals=globals())


class WiFi(object):

    def __init__(self):
        self.wifi = CWInterface.interfaceNames()

        for iname in self.wifi:
            self.interface = CWInterface.interfaceWithName_(iname)

    def get_wifistatus(self):
        if self.interface.powerOn() == 1:
            return "WiFi On"
        return "WiFi Off"

    def get_ssid(self):
        return self.interface.ssid()

    def get_interface(self):
        return self.interface.interfaceName()

    def get_hardwareaddress(self):
        return self.interface.hardwareAddress()

    def get_aggregatenoise(self):
        return self.interface.aggregateNoise()

    def get_aggregaterssi(self):
        return self.interface.aggregateRSSI()

    def get_bssid(self):
        return self.interface.bssid()

    def get_channel(self):
        return self.interface.channel()

    def get_transmitrate(self):
        return self.interface.transmitRate()

    def get_mcsindex(self):
        return self.interface.mcsIndex()

    # def get_wifi_list():
    #     client = CWWiFiClient.sharedWiFiClient()
    #     en0 = client.interface()
    #     listWifi = []
    #     listWifi.clear()
    #     iface = CWInterface.interface()
    #     networks, error = en0.scanForNetworksWithName_error_(None, None)
    #     for single_network in networks:
    #         if single_network:
    #             listWifi.append(WifiModel(single_network.ssid()))
    #             print(single_network)
    #     for lis in listWifi:
    #         print(lis.ssid)
    #         print(CWInterface.interfaceWithName_('en0'))
        # network = networks.anyObject()

# def get_wifistatus():
#     interface = CWInterface.interfaceWithName_('en0')
#     if interface.powerOn() == 1:
#         return "Yes"
#     return "No"


# def get_ssid():
#     interface = CWInterface.interfaceWithName_('en0')
#     return interface.ssid()


# def get_interface():
#     wifi = CWInterface.interfaceNames()
#     for iname in wifi:
#         print(iname)
#         interface = CWInterface.interfaceWithName_(iname)
#     return interface.interfaceName()


# def get_hardwareaddress():
#     wifi = CWInterface.interfaceNames()
#     for iname in wifi:
#         print(iname)
#         interface = CWInterface.interfaceWithName_(iname)
#     return interface.hardwareAddress()


# def get_aggregatenoise():
#     wifi = CWInterface.interfaceNames()
#     for iname in wifi:
#         print(iname)
#         interface = CWInterface.interfaceWithName_(iname)
#     return interface.aggregateNoise()


# def get_aggregaterssi():
#     wifi = CWInterface.interfaceNames()
#     for iname in wifi:
#         print(iname)
#         interface = CWInterface.interfaceWithName_(iname)
#     return interface.aggregateRSSI()


# def get_bssid():
#     interface = CWInterface.interfaceWithName_('en0')
#     return interface.bssid()


# def get_channel():
#     wifi = CWInterface.interfaceNames()
#     interface = CWInterface.interfaceWithName_('en0')
#     return interface.channel()


# def get_transmitrate():

#     interface = CWInterface.interfaceWithName_('en0')
#     return interface.transmitRate()


# def get_mcsindex():
#     wifi = CWInterface.interfaceNames()
#     for iname in wifi:
#         print(iname)
#         interface = CWInterface.interfaceWithName_(iname)
#     return interface.mcsIndex()

    # get_wifi_list()
