from .codec import pack_u32


class Queue2Mixin:
    """Q2: the driver table-transfer interface."""

    def q2_0x03_driver_if_version(self):
        """Return constant 23."""
        return self.send_message(2, 0x03)

    def q2_0x04_get_device_name(self, index: int):
        """Return a 4-byte chunk of the device name for index 0-11."""
        return self.send_message(2, 0x04, [index])

    def q2_0x05_enable_smu_features(self, mask_low: int, mask_high: int = 0):
        """Enable SMU features using a 64-bit mask split into two 32-bit words."""
        return self.send_message(2, 0x05, [mask_low, mask_high])

    def q2_0x06_disable_smu_features(self, mask_low: int, mask_high: int = 0):
        """Disable SMU features using a 64-bit mask split into two 32-bit words."""
        return self.send_message(2, 0x06, [mask_low, mask_high])

    def set_table1_dram_addr_high(self, value: int):
        """Set driver table #1 DRAM address (high 32 bits)."""
        return self.send_message(2, 0x0D, [value])

    def set_table1_dram_addr_low(self, value: int):
        """Set driver table #1 DRAM address (low 32 bits)."""
        return self.send_message(2, 0x0E, [value])

    def set_table2_dram_addr_high(self, value: int):
        """Set driver table #2 DRAM address (high 32 bits)."""
        return self.send_message(2, 0x0F, [value])

    def set_table2_dram_addr_low(self, value: int):
        """Set driver table #2 DRAM address (low 32 bits)."""
        return self.send_message(2, 0x10, [value])

    def q2_0x17_cpu_droop_calibration(self, test_voltage_mv: int, margin_mv: int):
        """Run CPU droop calibration (low16=test mV, high16=margin mV)."""
        param = ((margin_mv & 0xFFFF) << 16) | (test_voltage_mv & 0xFFFF)
        return self.send_message(2, 0x17, [param])

    # ---- Q2 0x0A transfer-engine sub-ops ----
    def transfer_engine_setup(self):
        """sub 0x00: key-window reset + init."""
        return self.send_message(2, 0x0A, [0x00])

    def transfer_engine_finalize(self):
        """sub 0x02: window restore + state machine."""
        return self.send_message(2, 0x0A, [0x02])

    def transfer_engine_table_restore(self):
        """sub 0x04: restore the key table."""
        return self.send_message(2, 0x0A, [0x04])

    def transfer_engine_cpu_copy(self, src: int, words: int):
        """sub 0x06: CPU copy SRAM[src] to the key table."""
        return self.send_message(2, 0x0A, [0x06, 0, src, words])

    def transfer_engine_pptable_smu2dram(self, state: int):
        """sub 0x11: TransferTableSmu2Dram state-machine step (0..3)."""
        return self.send_message(2, 0x0A, [0x11, state])

    def transfer_engine_pptable_dram2smu(self):
        """sub 0x12: TransferTableDram2Smu."""
        return self.send_message(2, 0x0A, [0x12])

    def transfer_engine_window_restore(self):
        """sub 0x13: restore the key window."""
        return self.send_message(2, 0x0A, [0x13])

    def transfer_engine_smu2dram(self, dram_hi: int, dram_lo: int, words: int):
        """sub 0x14: DMA the key-3 entry to DRAM[hi:lo]."""
        return self.send_message(2, 0x0A, [0x14, dram_hi, dram_lo, words, 0, 0])

    def transfer_engine_sram_load(self, src: int, words: int):
        """sub 0x1F: CPU copy SRAM[src] to the key-3 entry."""
        return self.send_message(2, 0x0A, [0x1F, 0, src, words])

    def transfer_engine_dram2smu(self, dram_hi: int, dram_lo: int, words: int, key: int):
        """sub 0x23: DMA DRAM[hi:lo] to a key entry."""
        return self.send_message(2, 0x0A, [0x23, dram_hi, dram_lo, words, 0, key])

    def q2_0x23_append(self, args):
        """msg 0x23: subqueue-ring append (the append-bug primitive)."""
        return self.send_message(2, 0x23, args, check_status=False)


    def _q2_0x2c_probably_power_limit_settings(self):
        return self.send_message(2, 0x2C)

    def _q2_0x2d_sibling_of_0x2c_but_returns_value(self):
        return self.send_message(2, 0x2D)
