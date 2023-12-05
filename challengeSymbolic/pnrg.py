   
# solo una bozza

def m_seed_random(state, seed):
  state.array[0] = seed & 0xffffffff
  index = 1
  while (index < 0x270):
    state.array[index] = state.array[index - 1] * 0x17b5
    index = index + 1
   


def genRandLong(state)
   
   if ((0x26f < state.index) || (state.index < 0)) {
      if ((0x270 < state.index) || (state.index < 0)) {
         m_seedRand(state,0x1105);
      }
      for (i = 0; i < 0xe3; i++) {
         uVar3 = (uint)param_1->array[local_14 + 1];
         param_1->array[local_14] =
                 param_1->array[local_14 + 0x18d] ^
                 (ulong)((uVar3 & 0x7fffffff | (uint)param_1->array[local_14] & 0x80000000) >> 1) ^
                 *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
      }


          for index in range(0xe3):
       uVar2 = state.array[index + 1]
       state.array[index] =
              state.array[index + 0x18d] ^
              ((uVar2 & 0x7fffffff | state.array[index] & 0x80000000) >> 1) ^
              *(ulong *)(mag.3808 + (ulong)(uVar2 & 1) * 8)








      for (; local_14 < 0x26f; local_14 = local_14 + 1) {
         uVar3 = (uint)param_1->array[local_14 + 1];
         param_1->array[local_14] =
                 param_1->array[local_14 + -0xe3] ^
                 (ulong)((uVar3 & 0x7fffffff | (uint)param_1->array[local_14] & 0x80000000) >> 1) ^
                 *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
      }
      uVar3 = (uint)param_1->array[0];
      param_1->array[0x26f] =
              param_1->array[0x18c] ^
              (ulong)((uVar3 & 0x7fffffff | (uint)param_1->array[0x26f] & 0x80000000) >> 1) ^
              *(ulong *)(mag.3808 + (ulong)(uVar3 & 1) * 8);
      param_1->index = 0;
   }
   iVar2 = param_1->index;
   param_1->index = iVar2 + 1;
   uVar1 = param_1->array[iVar2] ^ param_1->array[iVar2] >> 0xb;
   uVar1 = uVar1 ^ (uint)(uVar1 << 7) & 0x9d2c5680;
   uVar1 = uVar1 ^ (uint)(uVar1 << 0xf) & 0xefc60000;
   return uVar1 ^ uVar1 >> 0x12;
}