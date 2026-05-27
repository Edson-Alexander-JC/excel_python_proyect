from dataclasses import dataclass


@dataclass
class InputItem:
    kind:str = ""
    key:str = ""
    unit:str = ""
    label:str = ""
    width:float = 0.4
    value:any = None
    values:any = None