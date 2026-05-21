from abc import ABC,abstractmethod
class FabricInterface(ABC):
    @abstractmethod
    def render(self):pass
    @abstractmethod
    def set_vars(self):pass
    @abstractmethod
    def header(self):pass