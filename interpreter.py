from machine import StackMachine

m = StackMachine()

def interpret_program(program_string:str, machine:StackMachine = StackMachine(), t=65536):
    timeout = t
    machine.load_program(program_string)
    
    should_continue = True

    while(should_continue and timeout > 0):
        try:
            should_continue = machine.step_once()
        except Exception as e:
            print("\n=== Caught Exception: ===")
            print(e)
            print("\n")
            machine.debug_printout()
            machine.ip += 1
        timeout -= 1
    print()
    if(timeout == 0):
        print("You used too many cycles. Sorry.")
        exit()

if(__name__ == '__main__'):
    ins = input("> ")
    if ins == 'exit':
        exit()
    interpret_program(ins, m)
