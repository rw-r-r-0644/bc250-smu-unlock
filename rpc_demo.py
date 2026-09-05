#!/usr/bin/env python3
"""
rpc_demo - call-anything primitive usage example.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bc250_smu import Bc250Smu
from unlock import unlock

FN_PLL_POWER_SET = 0x23b14
FN_CLK_DOMAIN_UNGATE = 0x23744

if os.geteuid() != 0:
    sys.exit("needs root")

smu = Bc250Smu()
try:
    unlock(smu)

    # test VCN thing (credits to dantisnfs)
    smu.call(FN_PLL_POWER_SET, 6, 1)
    smu.call(FN_CLK_DOMAIN_UNGATE, 0x16)
    smu.call(FN_CLK_DOMAIN_UNGATE, 0x17)
    smu.call(FN_CLK_DOMAIN_UNGATE, 0x18)
finally:
    smu.close()
