from abc import ABC,abstractmethod
from app_module.shared.every_put import EveryPut
from app_module.shared.colum_setter import ColumnSetter
from app_module.shared.data_full_verify import DataFullVerify 
class FabricInterface(ABC):
    def __init__(self):
        self.ep : EveryPut = EveryPut()
        self.cs : ColumnSetter = ColumnSetter()
        self.dfv : DataFullVerify = DataFullVerify()
        self.set_vars()
    @abstractmethod
    def set_vars(self):pass
    @abstractmethod
    def render_sidebar(self):pass
    @abstractmethod
    def render_view(self):pass
    @abstractmethod
    def make_arquitecture(self):pass
    def render(self): self.make_arquitecture()
    
    