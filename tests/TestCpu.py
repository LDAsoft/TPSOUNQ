import unittest
from components.Cpu import Cpu
from components.Memory import Memory
from components.Pcb import Pcb

class TestCpu(unittest): 
    
    def setUp(self):
        self.pcb = Pcb()
        self.cpu = Cpu( Memory() )

    def test_set_current_pcb_sets_current_pcb(self):
        self.cpu.set_pcb(self.pcb)
        self.assertEquals(self.cpu.get_pcb(), self.pcb, "Current PCB not set correctly")


if __name__ == '__main__': 
    unittest.main()
    

# si hay o no PCB
# si fetch con PCB asignado
# si fetch sin PCB asignado 
# si fetch cuando el programa termino
# si fetch aumenta el program counter