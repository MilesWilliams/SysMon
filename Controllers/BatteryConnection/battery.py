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
            return str(battery_stats["Current Capacity"]) + "%"

    def is_charging(self):
        charging = False
        try:
            battery_stats = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery_stats = 0

        if (battery_stats != 0):
            if battery_stats["Is Charging"] == 1:
                charging = "Charging"
                return charging
            elif battery_stats["Is Charging"] == 0 and battery_stats["Current Capacity"] < 100:
                charging = "Not Charging"
                return charging

            elif battery_stats["Current Capacity"] == 100:
                charging = "Fully Charged"
                # try:
                #     if battery_stats["Is Charged"] is not False:
                #         charging = "Fully Charged"

                #     elif battery_stats["Is Charged"] is False:
                #         charging = "Fully Charged"
                #     return charging
                # except Exception as e:
                #     charging = "Not Charging"
                #     print(e)

                return charging

        return charging

    def time_to_empty():
        try:
            battery_stats = list(IOPSCopyPowerSourcesByType(0))[0]
        except:
            battery_stats = 0

        if (battery_stats != 0):
            return battery_stats["Time to Empty"]
