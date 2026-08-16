#!/usr/bin/env python3
"""
apply or verify firmware patches from an intel-hex file.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bc250_smu import Bc250Smu


def read_hex(path):
    sites, base = [], 0
    for line in open(path):
        if not line.startswith(":"):
            continue
        count = int(line[1:3], 16)
        addr = int(line[3:7], 16)
        typ = int(line[7:9], 16)
        data = bytes.fromhex(line[9:9 + count * 2])
        if typ == 2:
            base = int(line[9:13], 16) << 4
        elif typ == 0:
            sites.append((base + addr, data))
    return sorted(sites)


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify without writing")
    ap.add_argument("--hex", default=os.path.join(base, "patches.hex"))
    ns = ap.parse_args()
    if os.geteuid() != 0:
        sys.exit("needs root")

    patches = read_hex(ns.hex)
    smu = Bc250Smu()
    ok = True
    try:
        for addr, new in patches:
            cur = smu.smu_read_bytes(addr, len(new))
            if ns.check or cur == new:
                status = "OK" if cur == new else f"** MISMATCH (want {new.hex()})"
                print(f"check {addr:05X} {cur.hex()} {status}")
                ok &= cur == new
            else:
                smu.smu_write_bytes(addr, new)
                got = smu.smu_read_bytes(addr, len(new))
                status = "OK" if got == new else "** VERIFY FAIL"
                print(f"apply {addr:05X} {cur.hex()} -> {got.hex()} {status}")
                ok &= got == new
    finally:
        smu.close()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
