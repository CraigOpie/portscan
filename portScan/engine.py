#!/usr/bin/env python3
"""
author = "Craig Opie"
author_email = "craigopie@gmail.com"
name = "portScan"
version = "1.0.0"
description = "A port scanning utility."

"""
import socket
import subprocess
import sys
from datetime import datetime


# Ensure the program is not being called as a module
if __name__ == "__main__":
    # Clear the screen
    subprocess.call('clear', shell=True)

    # Get the IP Address to scan
    remoteServer = input("Enter the address of the remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-"*60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-"*60)

    # Check what time the scan started
    start = datetime.now()

    try:
        for port in range(1,5955):
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = socket_.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}:     Open".format(port))
            socket_.close()
    except KeyboardInterrupt:
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

    # Find out how long it took to perform the scan
    durration = datetime.now() - start

    # Display results
    print("Scanning completed in: "+str(durration))
