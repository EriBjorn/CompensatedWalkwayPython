#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Communicate with PLC though
Modbus-communication. Sending and
receiving data.

Code by: Magnus Øye, Dated: 05.10-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Balancing-Platform
"""

# Importing packages
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient


class ModbusClient(object):
    """Establishes a secure connection with the
    Modbus slave. Will be able to read and write
    to all of the available I/O."""
    def __init__(self, ip='192.168.56.1'):
        self.ip = ip
        self.client = ModbusTcpClient(self.ip, 502)
        self.connection = self.client.connect()

    def isConnected(self):
        """Returns the connection status.
        Return: True if connected, False if not."""
        return self.connection

    def sendInt(self, address, value):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not.
        """
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_int(value)
        payload = builder.build()
        
        return self.client.write_register(address, value, unit=1)


    def sendFloat(self, value, address):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not."""
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_float(value)
        payload = builder.build()
        result = self.client.write_registers(address, payload, skip_encode=True, unit=1)
        return result

    def readInt(self, address=12288, size=20):
        """Reads the number of addresses that the size contains.
        The readings start from the given address.
        Return: An array of read values"""
        response = self.client.read_holding_registers(address, size, unit=1)
        return response.registers

    def readFloat(self, address=12301, size=2):
        """Reads two bytes from the given start address.
        Returns the decoded float value"""
        response = self.client.read_holding_registers(address, size, unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(response.registers,
                                                     byteorder=Endian.Big,
                                                     wordorder=Endian.Little)
        value = decoder.decode_32bit_float()
        return value

    def close(self):
        """Closes the connection with the port.
        Return: True when the connection is closed."""
        self.client.close()
        return True

    
# Simple example of usage
if __name__ == '__main__':
    
    client = ModbusClient(ip='158.38.140.72')

    while client.isConnected():
        print("Connected")
        client.sendInt(32000, 707)
        client.sendInt(32001, 555)
        client.sendInt(32002, 444)
        client.sendInt(32003, 393)
        print("Numbers are sent")
  

      


        



 

