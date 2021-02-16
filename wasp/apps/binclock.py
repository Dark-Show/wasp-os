import wasp
import icons

# 2-bit RLE, generated from ../bit-60.png, 144 bytes
bit = (
    b'\x02'
    b'<\x1a'
    b'?\xf6@\xfcA\x80\xac\x81\xa6\x81A\x11A\x81\xa8\xc0'
    b'\xeb\xc1\x10A\x81\xaa@\xdbA\x0e\x80\xfc\x81\xc0\xac\xc1'
    b'\xec@\xfdA\x0c\x80V\x81\xee\xc0\xeb\xc1@\xfcA\t'
    b'\x01\x80\x81\x81\xc0\xac\xf0\xc1@\xfdA\x07\x80+\x81\xc1'
    b'\xf3\xc0\xdb\xc1\x06@\xebA\x80\xac\xb5\xc0V\xc1\x05@'
    b'\xfcA\x81\xb3\x80\xeb\x81\x01\x06A\xc0\xac\xc1\xf1\x81\x01'
    b'\x08A\xc1\xef\x81\x01\nA\xc1\xed\x81\x01\x0cA\xc1\xeb'
    b'\xc1A\x0eA\xc1\xea@\xfdA\x10\x80\xfc\x81\xc1\xe8\xc0'
    b'\xdb\xc1\x12\x81@\xacAf\x80\xeb\x81?\xf7'
)

# 2-bit RLE, generated from ../bit-60-faded.png, 67 bytes
bit_faded = (
    b'\x02'
    b'<\x1a'
    b'?\xf6@\xfcA\x80\xfd\xa8A\x11A\xaa\x10A\xac\x0e'
    b'A\xad\x81\x0c\xb1\t\x01\xb2\x81\x07\xc0+\xc1\xb5\x06\xb7'
    b'\x05A\xb5\x01\x06A\xb3\x01\x08A\xb1\x01\nA\xaf\x01'
    b'\x0cA\xadA\x0eA\xab\x81\x10A\xaa\x12A\xa8?\xf7'
)

class BinaryClockApp():
    NAME = 'Bin Clock'
    ICON = icons.app

    def foreground(self):
        """Activate the application."""
        wasp.system.bar.clock = False
        self._draw(True)
        wasp.system.request_tick(1000)

    def sleep(self):
        """Notify the application the device is about to sleep."""
        return True

    def wake(self):
        """Notify the application the device is waking up."""
        self._draw()

    def tick(self, ticks):
        """Notify the application that its periodic tick is due."""
        self._draw()

    def _draw(self, redraw=False):
        def draw_col(draw, col, num):
            # y cords for each bit
            bit8 = 60
            bit4 = 90
            bit2 = 120
            bit1 = 150

            if (num == 0):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit_faded, col * 60, bit1)
            elif (num == 1):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit, col * 60, bit1)
            elif (num == 2):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit, col * 60, bit2)
                draw.blit(bit_faded, col * 60, bit1)
            elif (num == 3):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit, col * 60, bit2)
                draw.blit(bit, col * 60, bit1)
            elif (num == 4):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit_faded, col * 60, bit1)
            elif (num == 5):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit, col * 60, bit1)
            elif (num == 6):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit, col * 60, bit4)
                draw.blit(bit, col * 60, bit2)
                draw.blit(bit_faded, col * 60, bit1)
            elif (num == 7):
                draw.blit(bit_faded, col * 60, bit8)
                draw.blit(bit, col * 60, bit4)
                draw.blit(bit, col * 60, bit2)
                draw.blit(bit, col * 60, bit1)
            elif (num == 8):
                draw.blit(bit, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit_faded, col * 60, bit1)
            elif (num == 9):
                draw.blit(bit, col * 60, bit8)
                draw.blit(bit_faded, col * 60, bit4)
                draw.blit(bit_faded, col * 60, bit2)
                draw.blit(bit, col * 60, bit1)

        """Draw the display from scratch."""
        draw = wasp.watch.drawable
        hi = wasp.system.theme('bright')

        if redraw:
            self._now = wasp.watch.rtc.get_localtime()
            draw.fill()
            wasp.system.bar.draw()
        else:
            self._now = wasp.system.bar.update()
            if not self._now or self._mm == self._now[4]:
                return

        # Draw the changeable parts of the watch face
        # hours
        draw_col(draw, 0, self._now[3] // 10)
        draw_col(draw, 1, self._now[3] % 10)

        # mintues
        draw_col(draw, 2, self._now[4] // 10)
        draw_col(draw, 3, self._now[4] % 10)

        # formatted date string
        draw.set_color(hi)
        draw.string('{}/{}/{}'.format(self._now[2], self._now[1],
                                      self._now[0]), 0, 200, width=240)

        self._mm = self._now[4]

