from .codec import mv_to_vid, vid_to_mv


class Queue0Mixin:
    """Q0: the standard PPSMC control messages (linux cyan_skillfish names)."""

    def _get_smu_version(self):
        return self.send_message(0, 0x02)

    def _get_driver_if_version(self):
        return self.send_message(0, 0x03)

    def _set_driver_table_dram_addr_high(self, value: int):
        self.send_message(0, 0x04, [value])

    def _set_driver_table_dram_addr_low(self, value: int):
        self.send_message(0, 0x05, [value])

    def _transfer_table_smu2dram(self):
        self.send_message(0, 0x06)

    def _transfer_table_dram2smu(self):
        self.send_message(0, 0x07)

    def request_core_pstate(self, pstate: int, core_mask: int):
        """Request a CPU P-state for cores specified in the mask."""
        param = ((pstate & 0xF) << 16) | (core_mask & 0xFF)
        return self.send_message(0, 0x0B, [param])

    def query_core_pstate(self, core_id: int):
        """Return the current core P-state (status 0xFF if core_id > 7)."""
        st, ret = self.send_message(0, 0x0C, [core_id], check_status=False)
        return ret

    def _request_gfxclk(self):
        self.send_message(0, 0x0E)

    def query_gfxclk(self):
        """Return the current GFX frequency in MHz."""
        st, ret = self.send_message(0, 0x0F)
        return ret

    def query_vddcr_soc_clock(self, index: int):
        """Return the SoC clock for the given DPM index (upper 16 bits)."""
        st, ret = self.send_message(0, 0x11, [(index & 0xFFFF) << 16])
        return ret

    def _query_df_pstate(self):
        return self.send_message(0, 0x13)

    def _configure_s3_pwroff_register_addr_high(self, value: int):
        self.send_message(0, 0x16, [value])

    def _configure_s3_pwroff_register_addr_low(self, value: int):
        self.send_message(0, 0x17, [value])

    def _request_active_wgp(self):
        self.send_message(0, 0x18)

    def _set_min_deep_sleep_gfxclk_freq(self, value: int):
        self.send_message(0, 0x19, [value])

    def _set_max_deep_sleep_dfll_gfx_div(self, value: int):
        self.send_message(0, 0x1A, [value])

    def _start_telemetry_reporting(self, value: int = 0):
        self.send_message(0, 0x1B, [value])

    def _stop_telemetry_reporting(self):
        self.send_message(0, 0x1C)

    def _clear_telemetry_max(self):
        self.send_message(0, 0x1D)

    def query_active_wgp(self):
        """Return the active workgroup processor count."""
        st, ret = self.send_message(0, 0x1E)
        return ret

    def get_gfx_frequency(self):
        """Return the current GFX frequency in MHz (alias of query_gfxclk)."""
        st, ret = self.send_message(0, 0x37)
        return ret

    def get_gfx_vid(self):
        """Return the current GFX VID in mV."""
        st, ret = self.send_message(0, 0x38)
        return vid_to_mv(ret)

    def force_gfx_freq(self, freq_mhz: int):
        """Force GFX frequency; firmware interprets the argument as MHz."""
        return self.send_message(0, 0x39, [freq_mhz])

    def unforce_gfx_freq(self):
        """Clear any forced GFX frequency settings."""
        return self.send_message(0, 0x3A)

    def force_gfx_vid(self, mv: int):
        """Force GFX VID using millivolts input."""
        vid = mv_to_vid(mv)
        return self.send_message(0, 0x3B, [vid])

    def unforce_gfx_vid(self):
        """Clear any forced GFX VID settings."""
        return self.send_message(0, 0x3C, check_status=False)

    def get_enabled_smu_features(self):
        """Return the enabled SMU feature bitmask."""
        st, ret = self.send_message(0, 0x3D)
        return ret

    def set_core_enable_mask(self, mask: int):
        """Set the CPU core enable mask (lower 8 bits)."""
        return self.send_message(0, 0x2C, [mask & 0xFF])

    def _gfx_cac_weight_operation(self, value: int):
        """For CAC Weights we don't really know what it does, only related thing we found was
        described in one of AMD Patent, with just mention of it's existing
        if someone from AMD reads this and wants to explain it, please help."""
        return self.send_message(0, 0x2F, [value])

    def _l3_cac_weight_operation(self, value: int):
        """For CAC Weights we don't really know what it does, only related thing we found was
        described in one of AMD Patents, with just mention of it's existing
        if someone from AMD reads this and wants to explain it, please help."""
        return self.send_message(0, 0x30, [value])

    def _pack_core_cac_weight(self, value: int):
        """For CAC Weights we don't really know what it does, only related thing we found was
        described in one of AMD Patents, with just mention of it's existing
        if someone from AMD reads this and wants to explain it, please help."""
        return self.send_message(0, 0x31, [value])

    def _set_driver_table_vmid(self, value: int):
        self.send_message(0, 0x34, [value])

    def set_soft_min_cclk(self, core_id: int, freq_mhz: int):
        """Set soft min CCLK for a core; returns the clamped frequency in MHz."""
        param = ((core_id & 0xFF) << 20) | (freq_mhz & 0xFFFF)
        st, ret = self.send_message(0, 0x35, [param])
        return ret

    def set_soft_max_cclk(self, core_id: int, freq_mhz: int):
        """Set soft max CCLK for a core; returns the clamped frequency in MHz."""
        param = ((core_id & 0xFF) << 20) | (freq_mhz & 0xFFFF)
        st, ret = self.send_message(0, 0x36, [param])
        return ret
