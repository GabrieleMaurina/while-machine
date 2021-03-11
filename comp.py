from while_machine import WhileMachine
import sys


def main():
	wm = WhileMachine()
	with open(sys.argv[1],'r') as while_prog, open(sys.argv[2],'w') as ram_prog:
		while_prog = while_prog.read()
		compiled = wm.compile_ram(while_prog)
		ram_prog.write(compiled)

if __name__ == '__main__':
	main()
