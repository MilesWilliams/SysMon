import psutil
import math
from .processes_model import Process

"""
    Error occurs :   File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/psutil/_common.py", line 316, in wrapper
                    ret = cache[fun]
                    KeyError: <function Process._get_pidtaskinfo at 0x104a749d8>

    ToDo : Make into class
"""


def bytes2human(n):
    symbols = (' B', ' KiB', ' MiB', ' GiB', ' TiB', ' PiB', ' EiB', ' ZiB',
               ' YiB')
    i = math.floor(math.log(abs(n) + 1, 2) / 10)
    return '%.1f%s' % (n / 2**(i * 10), symbols[int(i)])


def cpu_usage():
    return str(psutil.cpu_percent()) + '%'


def ram_usage():
    return str(psutil.virtual_memory().percent) + '%'


def available_memory():
    return bytes2human(psutil.virtual_memory().available)


def disk_read():
    return bytes2human(psutil.disk_io_counters().read_bytes)


def disk_written():
    return bytes2human(psutil.disk_io_counters().write_bytes)


def network_recv():
    return bytes2human(psutil.net_io_counters().bytes_recv)


def network_sent():
    return bytes2human(psutil.net_io_counters().bytes_sent)


def free_swap():
    return bytes2human(psutil.swap_memory().free)


def free_hdd():
    free = psutil.disk_usage('/').free * 1.1171428571
    return bytes2human(free)


def used_hdd():
    return bytes2human(psutil.disk_usage('/').used)


def total_hdd():
    total = psutil.disk_usage('/').total + 8811000000
    return bytes2human(total)


def get_open_apps():
    processList = []
    processList.clear()
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'memory_percent', 'status'])
        except psutil.NoSuchProcess:
            pass
        else:
            if pinfo['memory_percent'] is not None:
                if pinfo['name'] is not 'cache[fun]':
                    processList.append(Process(pinfo['pid'], pinfo['name'], pinfo['memory_percent'], pinfo['status']))

    processList.sort(key=lambda x: x.memory_percent, reverse=True)

    return processList
