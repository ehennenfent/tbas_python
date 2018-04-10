from machine import StackMachine

m = StackMachine()

def interpret_program(program_string, machine):
    timeout = 8192
    machine.load_program(program_string)

    while(machine.ip < len(program_string) and timeout > 0):
        try:
            machine.step_once()
        except Exception as e:
            print("Caught Exception:")
            print(e)
        timeout -= 1
    print()
    if(timeout == 0):
        print("You used too many cycles. Sorry.")
        exit()

def load_string(in_str):
    program += '>'.join('+'*(ord(k)) for k in in_str)
    program += '<'*len(in_str)

    interpret_program(program, m)


if(__name__ == '__main__'):
    ins = input("> ")
    if ins == 'exit':
        exit()
    interpret_program(ins)
