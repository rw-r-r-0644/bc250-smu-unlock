class Queue1Mixin:
    """Q1: mostly unexamined."""

    def _q1_0x08(self):
        return self.send_message(1, 0x08)

    def _q1_0x10(self):
        return self.send_message(1, 0x10)

    def _q1_0x68_secure(self):
        return self.send_message(1, 0x68, check_status=False)
