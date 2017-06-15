import objc
from AppKit import CWInterface
# objc.loadBundle('CoreWLAN',
#                 bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
#                 module_globals=globals())

# for iname in CWInterface.interfaceNames():
#     interface = CWInterface.interfaceWithName_(iname)

#     print ("""
# Interface:      %s
# SSID:           %s
# Transmit Rate:  %s
# Transmit Power: %s
# RSSI:           %s""" % (iname, interface.ssid(), interface.transmitRate(),
#                          interface.transmitPower(), interface.rssi()))

# # for net in CWInterface.scanForNetworks():
# #     print(net)


iface = CWInterface.interface()

networks, error = iface.scanForNetworksWithName_error_(None, None)
network = networks.anyObject()
print(networks)


# print(Test())
