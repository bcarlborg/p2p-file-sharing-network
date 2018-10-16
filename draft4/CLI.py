import sys
import os
import re

class CLI():
    def __init__(self):
        if sys.argv[1] == "init":
            self.handle_init_dir()
        elif sys.argv[1] == "start_network":
            self.handle_start_network()
        elif sys.argv[1] == "connect_to_network":
            self.handle_start_network()



    def handle_init_dir(self):
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):

            # TODO: add check for writing in ip and port
            listening_ip = sys.argv[3]
            listening_port_str = sys.argv[4]

            with open(os.path.join(dir_path, "addrs.config"), 'wb') as temp_file:
                temp_file.write(b"0: ")
                temp_file.write(listening_ip.encode("UTF-8"))
                temp_file.write(b" ")
                temp_file.write(listening_port_str.encode("UTF-8"))
                temp_file.write(b"\n")

        else:
            print("<<ERROR: invalid shared_dir provided>>")


    def handle_start_network(self):
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):
            # conn_ip = sys.argv[3]
            # conn_port_str = sys.argv[4]
            #
            # conn_addr = (conn_ip, int(conn_port_str))

            listneing_addr = self.parse_config_file(os.path.join(dir_path, "addrs.config"))["0"]

            # print(str(conn_addr))
            print(str(listneing_addr))

        else:
            print("<<ERROR: invalid shared_dir provided>>")


    def handle_conn_network(self):
        dir_path = sys.argv[2]

        if os.path.isdir(dir_path):
            # conn_ip = sys.argv[3]
            # conn_port_str = sys.argv[4]
            #
            # conn_addr = (conn_ip, int(conn_port_str))

            listneing_addr = self.parse_config_file(os.path.join(dir_path, "addrs.config"))["0"]

            # print(str(conn_addr))
            print(str(listneing_addr))

        else:
            print("<<ERROR: invalid shared_dir provided>>")

    def parse_config_file(self, config_file_path):
        try:
            config_file = open(config_file_path)
            file_contents = config_file.read()
            regex = r"(\d):\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+)"

            match = re.search(regex, file_contents)
            if match:
                matches = re.findall(regex, file_contents)
                addrs = {a[0] : (a[1], int(a[2])) for a in matches}
                return addrs

            else:
                print("<<ERROR: invalid config file format>>")
                print("exiting...")
                sys.exit(1)

        except FileNotFoundError:
            print("<<ERROR: no config file found>>")
            print("please reinitialize your shared_dir")
            print("exiting...")
            sys.exit(1)



if __name__ == "__main__":
    cl = CLI()