import objc
from Foundation import NSBundle


class InternalBattery(object):

    IOKit = NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')

    functions = [("IOServiceGetMatchingService", b"II@"),
                 ("IOServiceMatching", b"@*"),
                 ("IORegistryEntryCreateCFProperties", b"IIo^@@I"),
                 ("IOPSCopyPowerSourcesByType", b"@I"),
                 ("IOPSCopyPowerSourcesInfo", b"@"),
                 ]

    objc.loadBundleFunctions(IOKit, globals(), functions)

    def all_fields():
        try:
            battery = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery = 0
        if (battery != 0):
            return battery

    def current_capacity(self):
        try:
            battery_stats = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery_stats = 0

        if (battery_stats != 0):
            return battery_stats["Current Capacity"]

    def is_charging(self):
        charging = False
        try:
            battery_stats = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery_stats = 0

        if (battery_stats != 0):
            if battery_stats["Is Charging"] == 1:
                charging = True
                return charging
            elif battery_stats["Is Charging"] == 0:
                charging = False
                return charging

            return charging

    def time_to_empty():
        try:
            battery_stats = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery_stats = 0

        if (battery_stats != 0):
            return battery_stats["Time to Empty"]
