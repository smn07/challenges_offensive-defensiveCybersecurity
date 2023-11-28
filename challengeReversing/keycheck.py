from pwn import*

p = process("./keycheck_baby")

#input1 = b"\x1b\x51\x17\x2a\x1e\x4e\x3d\x10\x17\x46\x49\x14\x3d"
#input2 = b"babuzzbabuzzb"

#assert len(input1) == len(input2), "Le stringhe di byte devono avere la stessa lunghezza!"

#xor_result = bytes([b1 ^ b2 for b1, b2 in zip(input1, input2)])
#print(xor_result)



first_flag = b"flag{y0u_d4_qu33n_0f_cr4ck1ngz}"
flag = [0]*12

enc = b"\xeb\x51\xb0\x13\x85\xb9\x1c\x87\xb8\x26\x8d\x07"

key = -69

for i in range(0,12):
    flag[i] = (int(enc[i]) - key)%256
    key = flag[i] + key

#print(bytes(flag))

p.sendline(first_flag)

p.interactive()