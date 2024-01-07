from pwn import *

p = process(executable="./chall", argv=[], aslr=False)

binary = ELF("./chall")
# print the base of the binary
print("Binary base: 0x%x" % (binary.address))

ghidra_base = 0x00100000
ghidra_breakpoint = 0x0010136f
binary_base = 0x555555554000

binary_breakpoint = binary_base + (ghidra_breakpoint - ghidra_base)

gdb.attach(p, "hb *0x%x" % (binary_breakpoint))

input("wait")

p.interactive()