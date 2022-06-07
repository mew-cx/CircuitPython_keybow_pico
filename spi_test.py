"""CircuitPython Essentials Hardware SPI pin verification script"""
import board
import busio


def is_hardware_spi(clock_pin, data_pin):
    try:
        p = busio.SPI(clock_pin, data_pin)
        p.deinit()
        return True
    except ValueError:
        return False

print("is_hardware_spi(board.GP2, board.GP3) :", is_hardware_spi(board.GP2, board.GP3))
