import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []

for oneport in ports:
    portlist.append(str(oneport))
    print(str(oneport))

val = input('select Port : COM')

for x in range(0,len(portlist)):
    if  portlist[x].startswith("com" + str(val)):
        portVar = "com" + str(val)
        print(portlist[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('str').rstrip('\n'))