class Memory(object): 
    def __init__(self):
        self.ram = {}

    def put(self, address, instruction):
        self.ram[address] = instruction
    
    def get(self, address):
        return self.ram[address]
        