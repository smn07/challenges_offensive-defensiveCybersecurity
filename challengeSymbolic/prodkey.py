import angr
import claripy
from pwn import*

r = remote("bin.training.offdef.it", 2021)

#trovato da ghidra
TARGET = 0x400deb

#l'idea è che il check di quello che viene messo in input viene fatto nel TARGET -> quindi genero con BVS esattamente 32 caratteri
#(perchè devo leggere 32 caratteri da ghidra). A questo punto mi genera 32 caratteri a caso compresi tra 0x20 e 0x7e
#e costruisco la flag come la concatenazione di tutti i chars.
#quindi mi genera il potenziale input tale che io raggiungo il TARGET.

chars = [claripy.BVS(f"c_{i}", size=8) for i in range(32)]

flag = claripy.Concat(*chars)

proj = angr.Project("./prodkey")

initial_state = proj.factory.entry_state(stdin=flag)

for char in chars:
	initial_state.solver.add(char>=0x20)
	initial_state.solver.add(char<=0x7e)

simgr = proj.factory.simulation_manager(initial_state)
simgr.explore(find=TARGET)

if simgr.found:
    r.sendline(simgr.found[0].posix.dumps(0))

r.interactive()
