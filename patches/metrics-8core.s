#
# metric-8core.s
# fix 8-core metrics (tweak layout to leave sufficient space, loops are already good mostly)
#

# per-core loop store offsets (6-wide -> 8-wide)
.section .p_29c30, "ax"
s32i.n a12, a13, 0x10
.section .p_29c32, "ax"
s16i a11, a10, 0x30
.section .p_29c35, "ax"
s16i a8, a10, 0x48


# current table tail + l3 offsets
.section .p_29b6e, "ax"
s16i a9, a2, 0x5c
.section .p_29b71, "ax"
s16i a15, a2, 0x60
.section .p_29b74, "ax"
s16i a14, a2, 0x58
.section .p_29b77, "ax"
s16i a8, a2, 0x5e
.section .p_29b92, "ax"
s16i a12, a2, 0x62
.section .p_29bcd, "ax"
s32i a10, a15, 0x64
.section .p_29bd0, "ax"
s32i a8, a15, 0x6c
.section .p_29bd3, "ax"
s32i a14, a15, 0x74
.section .p_29bee, "ax"
s32i a8, a2, 0x7c
.section .p_29c9f, "ax"
s16i a14, a2, 0x80
.section .p_29ca2, "ax"
s16i a15, a2, 0x5a
.section .p_29ca5, "ax"
s16i a13, a2, 0x82
.section .p_29c69, "ax"
s16i a15, a14, 0x40
.section .p_29c6c, "ax"
s16i a13, a14, 0x44


# export dma length
.section .p_29cb2, "ax"
movi a12, 0x11c


# average table store offsets
.section .p_2987e, "ax"
s16i a10, a4, 0xe0
.section .p_2989c, "ax"
s16i a10, a4, 0xe4
.section .p_298ba, "ax"
s16i a10, a4, 0xe6
.section .p_298cb, "ax"
s16i a11, a4, 0xe8
.section .p_298e8, "ax"
s16i a10, a4, 0xea
.section .p_2991d, "ax"
s32i a8, a2, 0xec
.section .p_2993a, "ax"
s32i a11, a2, 0xf4
.section .p_29946, "ax"
s32i a10, a2, 0xfc
.section .p_299c2, "ax"
s16i a10, a2, 0x88
.section .p_299dd, "ax"
s32i a10, a6, 0x98
.section .p_29a00, "ax"
s16i a11, a2, 0xb8
.section .p_29a0c, "ax"
s16i a10, a2, 0xd0
.section .p_29a65, "ax"
s16i a8, a3, 0xc8
.section .p_29a71, "ax"
s16i a10, a3, 0xcc
.section .p_29aa9, "ax"
s16i a10, a4, 0xe2
.section .p_29ac7, "ax"
s16i a10, a4, 0x108
.section .p_29ad9, "ax"
s16i a10, a4, 0x10a


# average table ema read offsets
.section .p_29863, "ax"
l16ui a10, a4, 0xe0
.section .p_29884, "ax"
l16ui a10, a4, 0xe4
.section .p_298a2, "ax"
l16ui a10, a4, 0xe6
.section .p_298bd, "ax"
l16ui a10, a4, 0xe8
.section .p_298dd, "ax"
l16ui a10, a4, 0xea
.section .p_29900, "ax"
l32i a10, a2, 0xec
.section .p_2991a, "ax"
l32i a10, a2, 0xf4
.section .p_29937, "ax"
l32i a10, a2, 0xfc
.section .p_299a2, "ax"
l16ui a10, a2, 0x88
.section .p_299c8, "ax"
l32i a10, a6, 0x98
.section .p_299e0, "ax"
l16ui a10, a2, 0xb8
.section .p_299fd, "ax"
l16ui a10, a2, 0xd0
.section .p_29a4b, "ax"
l16ui a10, a3, 0xc8
.section .p_29a62, "ax"
l16ui a10, a3, 0xcc
.section .p_29a8e, "ax"
l16ui a10, a4, 0xe2
.section .p_29aaf, "ax"
l16ui a10, a4, 0x108
.section .p_29acd, "ax"
l16ui a10, a4, 0x10a
