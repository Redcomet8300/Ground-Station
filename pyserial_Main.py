import time
import serial.tools.list_ports

# List available serial ports
def list_available_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

# Select a serial port
def select_serial_port():
    available_ports = list_available_ports()
    print("Available serial ports:")
    for i, port in enumerate(available_ports):
        print(f"{i+1}: {port}")
    choice = input("Enter the number of the port you want to use: ")
    return available_ports[int(choice) - 1]

# Main program
selected_port = select_serial_port()
ser = serial.Serial(selected_port, 9600)

try:
    while True:
        simulated_data = str(time.time())  # Simulated data as a timestamp
        ser.write(simulated_data.encode())
        time.sleep(1)  # Adjust the delay as needed
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
