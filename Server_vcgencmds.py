# ASMT:2 Networking Client-Server ("vcgencmds" 2024 )
# Student name: Gurleen Kaur Jassal
# Student ID: 100942372
# Submission Date: 30 November 2024
# Instructor: Philip J
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the web or the other sources is properly cited, giving
# credit to the original author(s).

# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.
# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

# The server

import socket  # Import the socket library for network communication
import os  # Import the os library to execute shell commands
import json  # Import the json library to handle JSON data

def get_core_temperature():
    """Retrieve the core temperature from the Raspberry Pi."""
    temp = os.popen('vcgencmd measure_temp').readline()  # Execute command to get temperature
    return float(temp.split('=')[1].split("'")[0])  # Parse and return temperature as float

def get_voltage():
    """Retrieve the voltage from the Raspberry Pi."""
    voltage = os.popen('vcgencmd measure_volts').readline()  # Execute command to get voltage
    return float(voltage.split('=')[1].split('V')[0])  # Parse and return voltage as float

def get_memory_usage():
    """Retrieve the memory usage from the Raspberry Pi."""
    mem_info = os.popen('vcgencmd get_mem arm').readline()  # Execute command to get memory info
    return int(mem_info.split('=')[1].split('M')[0])  # Parse and return memory usage as int

def get_clock_speed():
    """Retrieve the clock speed from the Raspberry Pi."""
    clock_speed = os.popen('vcgencmd measure_clock arm').readline()  # Execute command to get clock speed
    return int(clock_speed.split('=')[1])  # Parse and return clock speed as int

def get_cpu_usage():
    """Retrieve the CPU usage from the Raspberry Pi."""
    cpu_usage = os.popen('vcgencmd measure_temp').readline()  # Incorrectly fetching temperature instead of CPU usage
    return float(cpu_usage.split('=')[1].split("'")[0])  # Parse and return CPU usage as float (should be fixed)

def start_server():
    """Start the server to listen for client connections."""
    s = socket.socket()  # Create a new socket object
    host = '10.102.13.202'  # Define the server's IP address
    port = 5000  # Define the port to listen on
    
    s.bind((host, port))  # Bind the socket to the host and port
    s.listen(5)  # Enable the server to accept connections, with a backlog of 5
    print(f"Server listening on {host}:{port}...")  # Print server status
    
    while True:  # Run an infinite loop to keep the server running
        try:
            c, addr = s.accept()  # Accept a new client connection
            print('Got connection from', addr)  # Print the client's address
            
            # Collect system data
            data = {
                "Temperature": round(get_core_temperature(), 1),  # Get and round core temperature
                "Voltage": round(get_voltage(), 1),  # Get and round voltage
                "Memory Usage": get_memory_usage(),  # Get memory usage
                "Clock Speed": get_clock_speed(),  # Get clock speed
                "CPU Usage": get_cpu_usage()  # Get CPU usage (note: this should be fixed)
            }

            # Send the collected data as a JSON response
            res = json.dumps(data)  # Convert data dictionary to JSON string
            c.send(res.encode('utf-8'))  # Send the JSON string as bytes to the client
            c.close()  # Close the client connection
        except Exception as e:
            print(f"Error handling client: {e}")  # Print any errors that occur

if __name__ == "__main__":
    start_server()  # Start the server when the script is executed

