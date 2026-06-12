from dataclasses import dataclass
@dataclass
class InputItem:
    kind:str = ""
    key:str = ""
    unit:str = ""
    label:str = ""
    value:any = None
    values:any = None