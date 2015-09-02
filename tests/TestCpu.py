import unittest
from components.Memory import Memory
from components.Pcb import Pcb
from components.Cpu import Cpu

class TestCpu(unittest.TestCase): 
    
    def setUp(self):
        self.pcb = Pcb()
        self.cpu = Cpu( Memory() )

    def test_set_current_pcb_sets_current_pcb(self):
        self.assertIsNone(self.cpu.get_pcb(), "Current PCB not set correctly")
        self.cpu.set_current_pcb(self.pcb)
        self.assertEquals(self.cpu.get_pcb(), self.pcb, "Current PCB not set correctly")

    def test_fetch(self):
        self.expectedFailures()
        
    
    def test_fetch_increments_pcb_pc(self):
        self.assertEquals(first, second, msg)


if __name__ == '__main__': 
    unittest.main()
    

# si hay o no PCB
# si fetch con PCB asignado
# si fetch sin PCB asignado 
# si fetch cuando el programa termino
# si fetch aumenta el program counter