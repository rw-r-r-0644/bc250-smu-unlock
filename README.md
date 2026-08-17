# BC-250 SMU unlock PoC

exploit queue 2 msg 0x23 bug to unlock secure access functions (which allow fully arb SMU rd/wr and code exec)

## note
current repo is BIOS 3 only! (patches etc. need different offsets for the SMU fw in BIOS 5!)

## writeup
TODO.. (see unlock.py for now)


## metrics-8core: average socket power

the retarget missed the socket power EMA pair: the old-value read
(0x29960 `l32i a10, a4, 0xdc`) and the write-back (0x2997a `s32i a10,
a13, 0x1dc`, a13 = table - 0x100) kept hitting the old 6-wide slot 0xdc,
so average socket power (now 0x104) stayed zero forever - linux
power1_average (AMDGPU_PP_SENSOR_GPU_AVG_POWER) read 0. the two extra
sites retarget both to 0x104. verified live on BIOS 3: power1_average
converges to real socket power.

(the EMA counter reads `l32i a12, a4, 0xf0` - old accnt slot - are also
still on the old offset; values converge fine, only the blending curve
is slightly off. left as-is.)
