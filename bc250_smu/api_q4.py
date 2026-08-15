
class Queue4Mixin:
    """Q4: shares the q3 table (same handlers)."""

    def _q4_0x04(self):
        return self.send_message(4, 0x04)

    def _q4_0x05(self):
        return self.send_message(4, 0x05)

    def _q4_0x06(self):
        return self.send_message(4, 0x06)

    def _q4_0x07(self):
        return self.send_message(4, 0x07)

    def _q4_0x08(self):
        return self.send_message(4, 0x08)

    def _q4_0x09(self):
        return self.send_message(4, 0x09)

    def _q4_0x0a_freq_op1(self, value: int = 0):
        return self.send_message(4, 0x0A, [value])

    def _q4_0x0b(self):
        return self.send_message(4, 0x0B)

    def _q4_0x0d(self):
        return self.send_message(4, 0x0D)

    def _q4_0x10(self):
        return self.send_message(4, 0x10)

    def _q4_0x11(self):
        return self.send_message(4, 0x11)

    def _q4_0x27_secure(self):
        return self.send_message(4, 0x27, check_status=False)
