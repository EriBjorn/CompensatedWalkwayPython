# #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  MIT License

  Copyright (c) 2019 magnusoy

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""

# Importing libraries
import serial
import os
from time import sleep


class SerialCommunication(object):
    """
    Serialconnection handler.
    """

    def __init__(self, port, baudrate=115200):
        """
        Establishes a connection to the given port.
        @port : where your device is connected
        @baudrate : the specified connection speed
                    (9600, 19200, 28800, 57600, 115200)
        """

        self.port = port
        self.baudrate = baudrate
        try:
            self.connection = serial.Serial(port, baudrate)
            sleep(2)
        except serial.SerialException as se:
            self.connection = None

    def isConnected(self):
        """
        Checks if the connection is established.
        @return False if not connected
                else True
        """

        result = False
        if self.connection is not None:
            result = True
        return result

    def readInputStream(self):
        """
        Read data sent trough Serial.
        @return decoded message
        """

        raw = self.connection.readline()
        data = raw.decode('latin-1')
        return data.rstrip('\n')

    def sendOutputStream(self, data):
        """
        Send data trough Serial.
        """
        addEndmaker = data + '\n'
        self.connection.write(addEndmaker.encode())

    def disconnect(self):
        """
        Disconnect the connection
        @return True if sucsessfully disconnected
        """

        self.connection.close()
        return True


# Example of usage
if __name__ == "__main__":
    arduino = SerialCommunication("COM4", 115200)

    while(arduino.isConnected()):
        #if os.name == 'nt':
         #   os.system('cls')
            
      print(arduino.readInputStream())

    
