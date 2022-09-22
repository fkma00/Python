class Set:
    
    def __init__(self):
        self.list = []
    
    def insert(self, tall):
        if tall in self.list:
            return self.list
        else:
            self.list.append(tall)
            return self.list
    
    def contains(self, tall):
        if tall in self.list:
            print("true")
        else:
            print("false")
        
    def remove(self, tall):
        if tall in self.list:
            self.list.remove(tall)
            return self.list
        else:
            return self.list
        
    def size(self):
        print(len(self.list))