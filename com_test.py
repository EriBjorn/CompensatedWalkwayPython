from modbus_com import ModbusClient
from serial_com import SerialCommunication
import time

ser = SerialCommunication("COM4", 115200)
mod = ModbusClient(ip="158.38.140.72")

print(mod.isConnected())
while mod.isConnected():
    val = ser.readInputStream()
    data = val.split(' ')
    num = float(data[1])
    num1 = float(data[3])
    num2 = float(data[5])
    num3 = float(data[9])

    num = int(num)
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)


    mod.sendInt(32002, num+90) # Pluss 90 grader for unngå minus
    mod.sendInt(32006, num1+180) # Pluss 180 grader for å unngå minus
    mod.sendInt(32003, num2)
    mod.sendInt(32004, num3)
    
    #print(res)
