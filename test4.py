class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("cpu: ",self.cpu,"ram: ",self.ram)

com1 = Computer("i5",8)
com2 = Computer("i7", 16)

com1.config()
com2.config()
