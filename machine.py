from buffer import Buffer
from badge_io import io_modes
from util import debug_buffer
from datatypes import Memory

class Machine(object):
    
    def __init__(self, num_cells: int = 32, bound: int = 255):
        self.num_cells: int = num_cells
        self.bound: int = bound
        self.clean_init()
        
        self.operations = {
            '+': self.increment,
            '-': self.decrement,
            '<': self.move_left,
            '>': self.move_right,
            '[': self.jumpr,
            ']': self.jumpl,
            '=': self.set_io,
            '?': self.do_io,
            'D': self.debug_printout
        }
    
    def clean_init(self):
        self.memory: Memory = [0 for _k in range(self.num_cells)]
        self.reset_program()
        
    def reset_program(self):
        self.data_pointer: int = 0
        self.io_mode: int = 0
        self.buffer: Buffer = Buffer()
        self.program: str = ""
        self.ip: int = 0

    def __repr__(self):
        out = ""
        for k in self.memory[self.data_pointer:]:
            if(k == 0):
                return out
            out += chr(max(0, k))
        return out
        
    def load_program(self, program_string:str):
        self.program = program_string

    @property
    def mcell(self) -> int:
        return self.mem_at(self.data_pointer)

    @mcell.setter
    def mcell(self, newval:int):
        self.set_mem_at(self.data_pointer, newval)

    def mem_at(self, index:int) -> int:
        if(index < 0 or index >= self.num_cells):
            return 0
        return self.memory[index]

    def set_mem_at(self, index:int, newval:int):
        if(index < 0 or index >= self.num_cells):
            return
        self.memory[index] = max(0, min(self.bound, int(newval)))

    def increment(self):
        self.mcell = min(self.bound, self.mcell + 1)

    def decrement(self):
        self.mcell = max(0, self.mcell - 1)

    def move_left(self):
        self.data_pointer = max(0, self.data_pointer - 1)

    def move_right(self):
        self.data_pointer = min(self.num_cells, self.data_pointer + 1)
        
    def jumpr(self):
        if self.mcell == 0:
            step = self.ip + 1
            num_rb_needed = 1
            while(step < num_cells):
                step += 1
                if(self.program[step] == '['):
                    num_rb_needed += 1
                if(self.program[step] == ']'):
                    num_rb_needed -= 1
                if(num_rb_needed == 0):
                    break
            self.ip = step
    
    def jumpl(self):
        if self.mcell != 0:
            step = self.ip
            num_lb_needed = 1
            while(step > 0):
                step -= 1
                if(self.program[step] == ']'):
                    num_lb_needed += 1
                if(self.program[step] == '['):
                    num_lb_needed -= 1
                if(num_lb_needed == 0):
                    break
            self.ip = step
            
    def rel_jumpr(self, amt: int):
        self.ip = min(len(self.ip) - 1, self.ip + amt)
        
    def rel_jumpl(self, amt: int):
        self.ip = max(0, self.ip - amt)

    def set_io(self):
        self.io_mode = m.mcell

    def do_io(self):
        io_modes[self.io_mode](self)
        
    def debug_printout(self):
        print("Program:", self.program)
        print("Machine:", hex(id(self)))
        print("IP:", self.ip)
        print("Data Pointer:", self.data_pointer)
        print("Buffer:")
        debug_buffer(self.buffer.buffer, indent=2)
        print("Memory:")
        debug_buffer(self.memory, indent=2)
            
    def _exec_tbas(self, _id):
        print("About to spawn another TBAS instance with arguments:", self.buffer)
        # TODO Figure out a sane way of doing this
    
    def _print_exec_args(self, id):
        tasks = ['TBAS', 'DIALER', 'SPEAKER', 'BLINKEN', 'SCROLLER', 'WAR DIALER', 'BOX', 'TBASCL', 'TBASED']
        print("Executing task", tasks[id], "with arguments:", self.buffer)
    
    def execute_task(self, task):
        tasks = [_exec_tbas] + [_print_exec_args for i in range(8)]
        tasks[task](task)
        
    def step_once(self):
        c = self.program[self.ip]
        assert c in self.operations.keys(), "Bad character at index {0} in program string: {1}".format(self.ip, c)
        self.operations[c]()
        self.ip += 1
        
        return self.ip < len(self.program)
    
    def run(self):
        steps = 0
        while(self.step_once()):
            steps += 1
        return steps + 1