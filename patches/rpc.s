#
# rpc.s
# call-any-function custom message
# (args/res in scratch struct at 0x12080)
#

.section .p_1ba6e, "ax"
j 0x12000

.section .p_rpcbody, "ax"
# entry: a2 = inst, a3 = magic (both survive; we only need a2 later)
movi  a5, 0x120
slli  a5, a5, 8
addmi a5, a5, 0x100
addi  a5, a5, -0x80          # a5 = 0x12080 (messy load, but it uses imms xP)
l32i  a9,  a5, 0             # fn
l32i  a10, a5, 4             # arg0 -> callee a2
l32i  a11, a5, 8             # arg1 -> callee a3
l32i  a12, a5, 12            # arg2 -> callee a4
l32i  a13, a5, 16            # arg3 -> callee a5
l32i  a14, a5, 20            # arg4 -> callee a6
callx8 a9                    # fn(arg0..arg4)
memw
s32i  a10, a5, 0x18          # result (a10 = retval) -> scratch+0x18
movi  a8, 0x5d
slli  a8, a8, 5              # a8 = 0xBA0
memw
l32i.n a8, a8, 0             # a8 = *(0xBA0) = queue base
addx2 a9, a2, a2
addx4 a9, a9, a8             # a9 = base + inst*0xc (queue_desc)
memw
l32i.n a6, a9, 0x10          # a6 = *(queue_desc+0x10) = status_ptr
movi  a10, 1
memw
s32i.n a10, a6, 0            # *status_ptr = 1
j 0x1ba76                    # original dispatcher epilogue
