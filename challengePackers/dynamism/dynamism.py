from pwn import *

# p = process(executable="./patched_dynamism", argv=["/home/marco/patched_dynamism", "flag"], aslr=False)

ghidra_base = 0x00100000
ghidra_breakpoint = 0x00101574
binary_base = 0x555555554000

binary_breakpoint = binary_base + (ghidra_breakpoint - ghidra_base)

print(hex(binary_breakpoint))
# 0x555555555574

# open the file in gdb, set the argv = ["/home/marco/dynamism", "flag"]
# set the breakpoint at binary_breakpoint

# p = gdb.debug(["./patched_dynamism", "flag"], gdbscript="hb *{}".format(hex(binary_breakpoint)))

# input("wait")

# p.interactive()