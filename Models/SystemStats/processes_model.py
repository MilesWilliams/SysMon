class Process(object):
    def __init__(self, pid, name, memory_percent, status):
        self.pid = pid
        self.name = name
        self.memory_percent = memory_percent
        self.status = status
