"""
    Date created:   01/10/2024
    Date edited:    04/19/2024
    Sub-module:     main.py
    Remarks:        Server program entry
"""
import server.src.server as server

# Program version

MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH_VERSION = 0

if __name__ == '__main__':
    serv = server.get_server_instance()
    serv.set_port(8000)
    serv.start_server()
