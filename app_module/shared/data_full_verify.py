class DataFullVerify:
    def __init__(self):pass
        
    def verify_array(self,data):
        for item in data:
            if not item:
                return False
        return True
    
    def verify_dict(self,data):
        for value in data.values():
            if not value:
                return False
        return True

    def verify(self,data):
        if isinstance(data, list):
            return self.verify_array(data)
        if isinstance(data, dict):
            return self.verify_dict(data)
        return False