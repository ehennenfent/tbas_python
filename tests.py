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
            self.assertEqual(i, m.mem_at(i))

    def test_buffer_fifo(self):
        m = Machine()
        m.load_program('+'*8 + '=?-?-?-?-?-?-?-?' + '+'*8 + '=>?>?>?>?>?>?>?>?')
        m.run()
        self.assertEqual(9, m.mem_at(0))
        for i in range(8, 0, -1):
            self.assertEqual(i, m.mem_at(i))

class TestConversions(unittest.TestCase):

    def test_ascii_lowercase(self):
        m = Machine()
        from string import ascii_lowercase
        program = '+'*12 + '=' + '-'*12 + '>'.join('+'*i for i in range(len(ascii_lowercase)))
        program += '<'*(program.count('>'))
        program += '>'.join('?' for i in range(len(ascii_lowercase)))
        m.load_program(program)
        m.run()
        for index, val in enumerate(ascii_lowercase):
            self.assertEqual(ord(val), m.mem_at(index))

    def test_ascii_uppercase(self):
        m = Machine()
        from string import ascii_uppercase
        program = '+'*13 + '=' + '-'*13 + '>'.join('+'*i for i in range(len(ascii_uppercase)))
        program += '<'*(program.count('>'))
        program += '>'.join('?' for i in range(len(ascii_uppercase)))
        m.load_program(program)
        m.run()
        for index, val in enumerate(ascii_uppercase):
            self.assertEqual(ord(val), m.mem_at(index))

    def test_digits(self):
        m = Machine()
        from string import digits
        program = '+'*14 + '=' + '-'*14 + '>'.join('+'*i for i in range(len(digits)))
        program += '<'*(program.count('>'))
        program += '>'.join('?' for i in range(len(digits)))
        m.load_program(program)
        m.run()
        for index, val in enumerate(digits):
            self.assertEqual(ord(val), m.mem_at(index))

    def test_tbas(self):
        m = Machine()
        from badge_io import tbas_chars
        program = '+'*15 + '=' + '-'*15 + '>'.join('+'*i for i in range(len(tbas_chars)))
        program += '<'*(program.count('>'))
        program += '>'.join('?' for i in range(len(tbas_chars)))
        m.load_program(program)
        m.run()
        for index, val in enumerate(tbas_chars):
            self.assertEqual(ord(val), m.mem_at(index))

class TestALU(unittest.TestCase):

    def test_stub(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
