from pwn import *
import z3

p = process("./pnrg")

class State:
  array = [0]*0x270
  index = 0

def m_seedRand(state, seed):
  state.array[0] = seed & 0xffffffff
  state.index = 1
  while (state.index < 0x270):
    state.array[state.index] = (state.array[state.index + -1] * 0x17b5)
    state.index = state.index + 1
  return

def mag_func(value):
  mag0 = z3.BitVecVal(0x0, 32)
  mag1 = z3.BitVecVal(0x9908b0df, 32)
  # 0xdfb0089900000000

  return z3.If(value & 1 == 0, mag0, mag1)

def gen_rand_long(param_1):
    uVar1 = 0
    iVar2 = 0
    uVar3 = 0
    local_14 = 0
    
    if (0x26f < param_1.index) or (param_1.index < 0):
        if (0x270 < param_1.index) or (param_1.index < 0):
            m_seedRand(param_1, 0x1105)
        
        for local_14 in range(0xe3):
            uVar3 = param_1.array[local_14 + 1]
            param_1.array[local_14] = (param_1.array[local_14 + 0x18d] ^
                                      z3.LShR((uVar3 & 0x7fffffff | (param_1.array[local_14] & 0x80000000)), 1) ^ 
                                     mag_func(uVar3)) & 0xffffffff
        
        while local_14 < 0x26f:
            uVar3 = param_1.array[local_14 + 1]
            param_1.array[local_14] = (param_1.array[local_14 - 0xe3] ^
                                      z3.LShR((uVar3 & 0x7fffffff | (param_1.array[local_14] & 0x80000000)), 1) ^
                                      mag_func(uVar3)) & 0xffffffff
            local_14 += 1
        
        uVar3 = param_1.array[0]
        param_1.array[0x26f] = (param_1.array[0x18c] ^
                               z3.LShR((uVar3 & 0x7fffffff | (param_1.array[0x26f] & 0x80000000)), 1) ^
                               mag_func(uVar3)) & 0xffffffff
        
        param_1.index = 0
    
    iVar2 = param_1.index
    param_1.index = iVar2 + 1
    
    uVar1 = param_1.array[iVar2] ^ z3.LShR(param_1.array[iVar2], 0xb)
    uVar1 ^= (uVar1 << 7) & 0x9d2c5680
    uVar1 ^= (uVar1 << 0xf) & 0xefc60000
    
    return uVar1 ^ z3.LShR(uVar1, 0x12)

state = State()
m_seedRand(state, z3.BitVec("seed", 32))

for _ in range(0, 1000):
  gen_rand_long(state)

final_value = gen_rand_long(state)

bytes_value = p.recvuntil(b",")[2:-1]
value = 0xfa4f9b47

s = z3.Solver()

s.add(final_value == value)

check_result = s.check()
if check_result == z3.sat:
    print(s.model())
else:
    print("No solution found")