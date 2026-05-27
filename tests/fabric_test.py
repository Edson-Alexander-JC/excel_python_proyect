from interfaces.fabric_interface import FabricInterface
from components.input_list.input_list import InputList
class FabricTest(FabricInterface):
    def __init__(self):
        InputList().render()
        
    def set_vars(self):
        pass
    def render(self):
        pass
    def header(self):
        pass
    