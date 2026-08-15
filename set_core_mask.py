#!/usr/bin/env python3
"""
example: write an arbitrary CPU core presence mask (SMN 0x5A870).

stock BC-250 boots with 0x77 (6c/12t); 0xFF enables all 8 cores.

usage:
  sudo python3 set_core_mask.py          # show current mask
  sudo python3 set_core_mask.py 0x35     # enable 4 specific cores (0011 0101)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bc250_smu import Bc250Smu, SmuError
from bc250_smu.transport import Bc250PciTransport
from unlock import unlock

MASK_REG = 0x5A870

def read_mask():
    t = Bc250PciTransport()
    t.open()
    try:
        return t.read_smu_reg(MASK_REG) & 0xFF
    finally:
        t.close()

def main():
    if os.geteuid() != 0:
        sys.exit("needs root")

    if len(sys.argv) < 2:
        print("current core presence mask: 0x%02X" % read_mask())
        return

    mask = int(sys.argv[1], 0) & 0xFF
    force = "-f" in sys.argv
    before = read_mask()
    print("current core presence mask: 0x%02X" % before)
    if before == mask:
        print("already set - nothing to do")
        return

    smu = Bc250Smu()
    try:
        unlock(smu)
        smu.smn_write32(MASK_REG, mask)
    finally:
        smu.close()

    after = read_mask()
    print("after write: 0x%02X" % after)

    if after != mask:
        sys.exit("mask did not take")
    print("OK - reboot to bring up the new cores")


if __name__ == "__main__":
    main()
