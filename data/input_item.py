class InputItem:
    def __init__(self,
        kind:str,
        key:str="",
        unit:str ="",
        label:str ="",
        width:float = 0.4,
        value=None,values=None
    ):
        self.kind:str = kind
        self.label:str = label
        self.key:str = key
        self.unit:str = unit
        self.value:str = value
        self.values = values
        self.width = width
        