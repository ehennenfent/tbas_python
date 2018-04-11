import unittest
from machine import Machine

class TestLanguage(unittest.TestCase):

    def test_mptr_inc_dec(self):
        m = Machine()
        m.load_program('+++>+++>+++>++++')
        m.run()
        self.assertEqual(3, m.mem_at(0))
        self.assertEqual(3, m.mem_at(1))
        self.assertEqual(3, m.mem_at(2))
        self.assertEqual(4, m.mcell)
        m.reset_program()
        m.load_program('>>>-<--<---<----')
        m.run()
        self.assertEqual(0, m.mcell)
        self.assertEqual(0, m.mem_at(1))
        self.assertEqual(1, m.mem_at(2))
        self.assertEqual(3, m.mem_at(3))
        
    def test_loop(self):
        m = Machine()
        m.load_program('+++++')
        self.assertEqual(5, m.run())
        self.assertEqual(5, m.mem_at(0))
        m.reset_program()
        m.load_program('[-]')
        self.assertEqual(11, m.run())
        self.assertEqual(0, m.mcell)
        
    def test_nested_loop(self):
        m = Machine()
        m.load_program('+++++[>+++[>+<-]<-]')
        m.run()
        self.assertEqual(15, m.mem_at(2))
        

class TestBuffer(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

class TestConversions(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

class TestALU(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()