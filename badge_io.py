from string import ascii_lowercase, ascii_uppercase, digits
import sys

tbas_chars = ['+', '-', '<', '>', '[', ']', '=', '?']


def not_implemented(_machine, _state, _context):
    print("IO MODE NOT IMPLEMENTED")

def console_write(wr):
    sys.stdout.write(str(wr))
    sys.stdout.flush()
    
def decimal_read(m):
    m.mcell = int(input('d> '))

def ascii_read(m):
    m.mcell = ord(input('a> ')[0])

def buffer_program(m):
    for k in m.program:
        m.buffer.enqueue(ord(k))
    m.buffer.clear()

def set_mcell(newval):
    m.mcell = newval

io_modes = [
    lambda m: console_write(int(m.mcell)), # 0
    decimal_read,
    lambda m: console_write(chr(m.mcell)),
    ascii_read,
    not_implemented,
    not_implemented, # 5
    buffer_program,
    not_implemented,
    lambda m: m.buffer.enqueue(m.mcell),
    lambda m: set_mcell(m.buffer.dequeue_filo()),
    lambda m: set_mcell(m.buffer.dequeue_fifo()), # 10
    lambda m: m.buffer.clear(),
    lambda m: set_mcell(ord(ascii_lowercase[max(0, min(25, m.mcell))])), # Not quite right. Spec says out-of-bounds values
    lambda m: set_mcell(ord(ascii_uppercase[max(0, min(25, m.mcell))])), # should be left alone, not clamped.
    lambda m: set_mcell(ord(digits[max(0, min(9, m.mcell))])),          # Need an actual function for this.
    lambda m: set_mcell(ord(tbas_chars[max(0, min(7, m.mcell))])), # 15
    lambda m: set_mcell(m.mcell + m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m.mcell - m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m.mcell * m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m.mcell // m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m.mcell & m.buffer.dequeue_fifo()), # 20
    lambda m: set_mcell(m.mcell | m.buffer.dequeue_fifo()),
    lambda m: set_mcell(1 if (m.mcell == 0) else 0),
    lambda m: set_mcell(m.mcell ^ m.buffer.deque_fifo()),
    lambda m: set_mcell(m.data_pointer),
    lambda m: set_mcell(m.ip + 1),  # 25
    not_implemented,
    not_implemented,
]