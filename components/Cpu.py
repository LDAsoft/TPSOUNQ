class Cpu(object):
    def __init__(self, memory):
        self.memory = memory
        self.pcb = None
    
    def set_current_pcb(self, pcb):
        self.pcb = pcb
    
    def get_pcb(self):
        return self.pcb