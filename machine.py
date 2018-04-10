from buffer import Buffer
from badge_io import io_modes

class StackMachine(object):
    
    def __init__(self, num_cells=16, bound=255):
        self.num_cells = num_cells
        self.bound = bound
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
        self.memory = [0 for _k in range(self.num_cells)]
        self.data_pointer = 0
        self._io_mode = 0
        self.buffer = Buffer()
        self.program = ""
        self.ip = 0

    def __repr__(self):
        out = ""
        for k in self.memory[self.data_pointer:]:
            if(k == 0):
                return out
            out += chr(max(0, k))
        return out
        
    def load_program(self, program_string):
        self.program = program_string

    @property
    def mcell(self):
        return self.mem_at(self.data_pointer)

    @mcell.setter
    def mcell(self, newval):
        self.set_mem_at(self.data_pointer, newval)
        
    @property
    def io_mode(self):
        return self._io_mode
    
    @io_mode.setter
    def io_mode(self, new_io):
        self._io_mode = new_io

    def mem_at(self, index):
        if(index < 0 or index >= self.num_cells):
            return 0
        return self.memory[index]

    def set_mem_at(self, index, newval):
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
        if(m.mem_at(m.data_pointer) == 0):
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
        if(m.mem_at(m.data_pointer) != 0):
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

    def set_io(self):
        self.io_mode = m.mcell

    def do_io(self):
        io_modes[self.io_mode](self)
        
    def debug_printout(self):
        print("Program:", self.program)
        print("IP:", self.ip)
        print("Machine State:")
        print("\tData Pointer:", self.data_pointer)
        print("\tMemory:")
        for i in range(self.num_cells):
            print("\t\t", self.mem_at(i), "\t\t", chr(max(0, self.mem_at(i))))
            
    def step_once(self):
        c = self.program[self.ip]
        assert c in self.operations.keys()
        self.operations[c]()
        self.ip += 1