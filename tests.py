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

    def test_buffer_program(self):
        m = Machine()
        program_string = '++++++=?'
        m.load_program(program_string)
        m.run()
        self.assertEqual(program_string, str(m.buffer))

    def test_buffer_filo(self):
        m = Machine()
        m.load_program('+'*8 + '=?-?-?-?-?-?-?-?' + '+'*8 + '=>?>?>?>?>?>?>?>?')
        m.run()
        self.assertEqual(9, m.mem_at(0))
        for i in range(1, 9):
            self.assertEquals(i, m.mem_at(i))

    def test_buffer_fifo(self):
        m = Machine()
        m.load_program('+'*8 + '=?-?-?-?-?-?-?-?' + '+'*8 + '=>?>?>?>?>?>?>?>?')
        m.run()
        self.assertEqual(9, m.mem_at(0))
        for i in range(8, 0, -1):
            self.assertEqual(i, m.mem_at(i))

class TestConversions(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

class TestALU(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
