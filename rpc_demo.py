#!/usr/bin/env python3
"""
rpc_demo - call-anything primitive usage example.

NOTE: run this after patcher.py !
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bc250_smu import Bc250Smu

FN_PLL_POWER_SET = 0x23b14
FN_CLK_DOMAIN_UNGATE = 0x23744


def main(argv=None) -> int:
    if os.geteuid() != 0:
        print("needs root", file=sys.stderr)
        return 1

    smu = Bc250Smu()
    try:
        # test VCN thing (credits to dantisnfs)
        smu.call(FN_PLL_POWER_SET, 6, 1)
        smu.call(FN_CLK_DOMAIN_UNGATE, 0x16)
        smu.call(FN_CLK_DOMAIN_UNGATE, 0x17)
        smu.call(FN_CLK_DOMAIN_UNGATE, 0x18)
    finally:
        smu.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
