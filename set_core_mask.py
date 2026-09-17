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

def main(argv=None) -> int:
    if os.geteuid() != 0:
        print("needs root", file=sys.stderr)
        return 1

    args = sys.argv[1:] if argv is None else list(argv)

    if not args:
        print("current core presence mask: 0x%02X" % read_mask())
        return 0

    mask = int(args[0], 0) & 0xFF
    before = read_mask()
    print("current core presence mask: 0x%02X" % before)
    if before == mask:
        print("already set - nothing to do")
        return 0

    smu = Bc250Smu()
    try:
        unlock(smu)
        smu.smn_write32(MASK_REG, mask)
    finally:
        smu.close()

    after = read_mask()
    print("after write: 0x%02X" % after)

    if after != mask:
        print("mask did not take", file=sys.stderr)
        return 1
    print("OK - reboot to bring up the new cores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
