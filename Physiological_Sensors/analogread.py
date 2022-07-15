#!/usr/bin/env python
'''
This gets and prints both the analog voltages and digital values from channels 0 and 1 of the ADC to
both the console and to a file
'''
import curses
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

with open("rawdata.txt", "w", encoding='ascii') as storedvalues:
    # create an analog input channel on pin 0
    chan0 = AnalogIn(mcp, MCP.P0)
    chan1 = AnalogIn(mcp, MCP.P1)
    while True :
        stdscr.addstr(0, 0, 'Raw Channel 0 ADC Value: ' + str(chan0.value))
        stdscr.clrtoeol()
        stdscr.addstr(1, 0, ' ADC Channel 0 Voltage: ' + str(chan0.voltage) + 'V')
        stdscr.clrtoeol()
        storedvalues.write('Raw Channel 0 ADC Value: ' + str(chan0.value) +
        ' ADC Channel 0 Voltage: ' + str(chan0.voltage) + 'V\n')

        stdscr.addstr(2, 0, 'Raw Channel 1 ADC Value: ' + str(chan1.value))
        stdscr.clrtoeol()
        stdscr.addstr(3, 0, ' ADC Channel 1 Voltage: ' + str(chan1.voltage) + 'V')
        stdscr.clrtoeol()
        storedvalues.write('Raw Channel 1 ADC Value: ' + str(chan0.value) +
        ' ADC Channel 1 Voltage: ' + str(chan0.voltage) + 'V\n')
        stdscr.refresh()
curses.echo()
curses.nocbreak()
curses.endwin()
