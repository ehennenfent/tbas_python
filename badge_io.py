from string import ascii_lowercase, ascii_uppercase, digits
from typing import List
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

def set_mcell(m, newval: int):
    m.mcell = newval
    
def convert(index: int, lang: List[str]) -> int:
    if index not in range(0, len(lang)):
        return index
    return ord(lang[index])
    
io_modes = [
    lambda m: console_write(int(m.mcell)), # 0
    decimal_read,
    lambda m: console_write(chr(m.mcell)),
    ascii_read,
    not_implemented, #   - modem write
    not_implemented, # 5 - modem read
    buffer_program,
    not_implemented, #   - execute task
    lambda m: m.buffer.enqueue(m.mcell),
    lambda m: set_mcell(m, m.buffer.dequeue_filo()),
    lambda m: set_mcell(m, m.buffer.dequeue_fifo()), # 10
    lambda m: m.buffer.clear(),
    lambda m: set_mcell(m, convert(m.mcell, ascii_lowercase)),
    lambda m: set_mcell(m, convert(m.mcell, ascii_uppercase)),
    lambda m: set_mcell(m, convert(m.mcell, digits)),
    lambda m: set_mcell(m, convert(m.mcell, tbas_chars)), # 15
    lambda m: set_mcell(m, m.mcell + m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m, m.mcell - m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m, m.mcell * m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m, m.mcell // m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m, m.mcell & m.buffer.dequeue_fifo()), # 20
    lambda m: set_mcell(m, m.mcell | m.buffer.dequeue_fifo()),
    lambda m: set_mcell(m, 1 if (m.mcell == 0) else 0),
    lambda m: set_mcell(m, m.mcell ^ m.buffer.deque_fifo()),
    lambda m: set_mcell(m, m.data_pointer),
    lambda m: set_mcell(m, m.ip + 1),  # 25
    lambda m: m.rel_jumpl(m.mcell),
    lambda m: m.rel_jumpr(m.mcell),
]