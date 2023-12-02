import angr
import claripy
from pwn import*

r = remote("bin.training.offdef.it", 2021)

TARGET = 0x00403370
AVOID = [0x00403369, 0x0040317c, 0x00402f79, 0x00402d77, 0x00402b7c,
         0x0040297c, 0x00402781, 0x00402576, 0x00402379, 0x00402181,
         0x00401f7d, 0x00401d7a, 0x00401b6d, 0x00401978, 0x0040177f,
         0x00401592, 0x0040139d, 0x004011af, 0x00400fac, 0x00400da6,
         0x00400bad, 0x004009ac, 0x00400797]

chars = [claripy.BVS(f"c_{i}", size=8) for i in range(24)]

flag = claripy.Concat(*chars)

proj = angr.Project("./cracksymb",use_sim_procedures=True, auto_load_libs=False)

# initial_state = proj.factory.entry_state(stdin=flag)
initial_state = proj.factory.full_init_state(stdin=flag, add_options={angr.options.LAZY_SOLVES})

for char in chars:
  initial_state.solver.add(char >= 0x20)
  initial_state.solver.add(char <= 0x7e)

simgr = proj.factory.simulation_manager(initial_state)

while len(simgr.active) > 0:
  print(simgr, simgr.active)
  simgr.explore(find=TARGET, avoid=AVOID, n=1, num_find=1)
  if len(simgr.found) > 0:
    break

if simgr.found:
    print("SUCCESS")
    r.sendline(simgr.found[0].posix.dumps(0))

r.interactive()