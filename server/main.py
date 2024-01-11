"""
    Date created:   01/10/2023
    Date edited:    01/11/2023
    Sub-module:     main.py
    Remarks:        Server program entry
"""
import server.src.server as sv

# Program version

MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH_VERSION = 0

if __name__ == '__main__':
    serv = sv.get_server_instance()
    serv.set_port(8000)
    serv.run_server()
