import unittest
from components.Memory import Memory

class TestMemory(unittest.TestCase):
    
    def setUp(self):
        self.memory = Memory()


    def test_put_adds_instruction_in_specified_address(self):
        self.memory.put(00000, "instruccion1")
        self.assertEqual("instruccion1", self.memory.get(00000), "Instruction not found in memory cell")    

    def test_get_gets_instruction_from_specified_address(self):
        instruction = self.memory.put(00000, "instruccion1")
        self.assertEqual("instruccion1", instruction, "Instruction not found in memory cell")    


if __name__ == '__main__': 
    unittest.main()