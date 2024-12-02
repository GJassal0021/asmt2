# ASMT:2 Networking CLient-Server ("vcgencmds" 2024)
# Student name: Gurleen Kaur Jassal
# Student ID: 100942372
# Submission Date : 30 November 2024
# Instructor - Philip J
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

# Run on Pc, directly from thonny
# The client

# Importing necessary libraries
import socket  # Library for creating network connections
import json    # Library for parsing JSON data

def main():
    # Create a socket object for communication
    s = socket.socket()
    
    # Define the host IP address of the Raspberry Pi server
    host = '10.102.13.202'  # IP of Raspberry Pi running the server
    # Define the port number on which the server is listening
    port = 5000

    try:
        s.connect((host, port))# Establish a connection to the server using the specified host and port
        
        # Receive data from the server (up to 1024 bytes)
        data = s.recv(1024).decode()  # Decode the received bytes to a string
        
        # Parse the received JSON data into a Python dictionary
        pi_data = json.loads(data)
        
        # Iterate through each key-value pair in the parsed JSON data
        for key, value in pi_data.items():
            # Print each key and its corresponding value on a new line
            print(f"{key}: {value}")
        
    except ConnectionRefusedError:
        # Handle the case where the connection is refused (server not running)
        print("Unable to connect to the server. Make sure it's running.")
    except json.JSONDecodeError:
        # Handle the case where the received data is not valid JSON
        print("Received invalid JSON data from the server.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")
    finally:
        # Close the socket connection to free up resources
        s.close()

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to execute the client code

