from tkinter import Tk
from machine import Machine
from gui.memory import Mem
from gui.program import Program
from gui.status import StatusBar
from gui.toolbar import ToolBar
import time


class UI:

    def __init__(self, machine: Machine = Machine(program="+++[?-]")):
        self.machine = machine

        self.root = Tk()
        self.toolbar = ToolBar(self.root, self.run, self.continue_exec, self.step, self.reset)
        self.program = Program(self.root, machine.program)
        self.buffer = Mem(self.root, title="Buffer", size=machine.buffer.max_length)
        self.memory = Mem(self.root, title="Memory", size=machine.num_cells)
        self.status = StatusBar(self.root)

        self.update()

    def run(self):
        self.continue_exec()

    def continue_exec(self, n=65536):
        should_continue = True
        timeout = n
        while should_continue and timeout > 0 and self.machine.ip not in self.program.breakpoints:
            try:
                should_continue = self.machine.step_once()
                self.update()
            except Exception as e:
                self.update()
                raise e
            timeout -= 1

    def step(self):
        self.machine.step_once()
        self.update()

    def reset(self):
        saved_program = self.machine.program
        self.machine.clean_init()
        self.machine.load_program(saved_program)
        self.update()

    def update(self):
        self.status.set("IP: %d | Data Pointer %d | IO Mode %d",
                        self.machine.ip,
                        self.machine.data_pointer,
                        self.machine.io_mode)
        self.buffer.update(self.machine.buffer.buffer)
        self.memory.update(self.machine.memory)
        self.program.highlight(self.machine.ip)
        self.root.update()

    def _start(self):
        self.root.mainloop()

UI(machine=Machine(program='++++++=?++++=>++>+[?<=>?<<=>>]<<----=?+=>>>?'))._start()
