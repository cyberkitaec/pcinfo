from abc import ABC, abstractmethod

class DispatcherAbstract(ABC):

    @abstractmethod
    async def cpu_usage(self):
        raise NotImplementedError

    @abstractmethod
    async def memory_usage(self):
        raise NotImplementedError

    @abstractmethod
    async def form_general_data(self):
        raise NotImplementedError

    @abstractmethod
    async def form_metrics(self):
        raise NotImplementedError