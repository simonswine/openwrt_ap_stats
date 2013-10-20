import SocketServer
import re

RE_MARKER = re.compile("(#+)([^#]+)(#+)")

def parse_input(data):

    data_lines = data.split("\n")

    data_marker = parse_data_marker(data_lines)

    print parse_data(data_lines,data_marker)


def parse_data(data,data_marker):

    min_order = min([m[1] for m in data_marker])

    data_lines()

    line_start = 0

    # Get start of first min level
    for m in data_marker:
        if m[1]==min_order:
            break
        line_start += 1



    #print data

    pass


def parse_data_marker(data):
    """
    Finds labels and their order
    """
    count = 0
    return_val = []
    for line in data
        count += 1
        m = RE_MARKER.match(line)
        if m:
            if len(m.group(1))==len(m.group(3)):
                return_val.append((count,len(m.group(1)),m.group(2)))

    return return_val


class Host:
    """
    Represents one wlan host/ap
    """
    def  __init__(self,hostname=None,data={}):
        self.hostname = hostname
        self.data = data
        self.wlan_ssids = []
        pass




class WlanSsid:
    """
    Represents one wlan net with one ssid and channel
    """

    pass

class Station:
    """
    Represents one wlan station/client
    """
    pass

class WlanApMonitorHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = ''
        while 1:
            new_data = self.request.recv(1024)
            if not new_data: break
            self.data = self.data + new_data

        print "{} wrote:".format(self.client_address[0])
        parse_input(self.data)

        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), WlanApMonitorHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

