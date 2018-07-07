from tkinter import Tk
from machine import Machine
from gui.memory import Mem
from gui.program import Program
from gui.status import StatusBar
from gui.toolbar import ToolBar



class UI:

    def __init__(self, machine=Machine(program="+++[?-]")):
        self.root = Tk()
        self.toolbar = ToolBar(self.root, self.run, self.continue_exec, self.step, self.reset)
        self.program =  Program(self.root, machine.program)
        self.buffer = Mem(self.root, title="Buffer")
        self.memory = Mem(self.root, title="Memory")
        self.status = StatusBar(self.root)

    def run(self):
        print("Running")

    def continue_exec(self):
        print("continue")

    def step(self):
        print("step")

    def reset(self):
        print("reset")

    def _start(self):
        self.root.mainloop()

UI()._start()
