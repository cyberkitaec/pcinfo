from dispatcher.DispatcherAbstract import DispatcherAbstract
import psutil
import os


class DispatcherWindows(DispatcherAbstract):
    hostname: str
    username: str
    logic_cpu: int
    general_cpu: int

    def __init__(self):
        self.hostname = os.popen("hostname").read()
        self.username = os.popen("echo %USERNAME%").read()
        self.logic_cpu = psutil.cpu_count(logical=False)
        self.general_cpu = psutil.cpu_count()

    async def cpu_usage(self):
        res = psutil.cpu_percent(interval=1)
        return res

    async def memory_usage(self):
        memory = psutil.virtual_memory().percent
        return memory

    async def form_general_data(self):
        return {"hostname": self.hostname, "username": self.username,
                "logic_cpu": self.logic_cpu, "count_cpu": self.general_cpu}

    async def form_metrics(self):
        cpu_usage = await self.cpu_usage()
        memory = await self.memory_usage()

        return {"cpu_usage": cpu_usage, "memory_usage": memory}

    def get_hostname(self):
        return self.hostname

    def get_username(self):
        return self.username

    def get_logic_cpu(self):
        return self.logic_cpu

    def get_general_cpu(self):
        return self.general_cpu

