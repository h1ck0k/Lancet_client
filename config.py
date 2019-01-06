#python3


class config:


    def __init__(self):
        self.destination = "192.168.1.1"
        self.portRange = []
        self.protocols = []
        self.timing = []

    def setPortRange(self,start=0,stop=65535,**kwargs):

        for port in range(start, stop, 1):
            self.portRange.append(port)

        for each in **kwargs:
            self.portRange.append(each)

    def getPortRange(self):
        return self.portRange
