class Computer:
    def __init__(self,cpu,memory,disc):
        print('Computer is inited')
        self.cpu = cpu
        self.memory = memory
        self.disc = disc

class Tv:
    def __init__(self,screen_size):
        self.screen_size = screen_size

# 笔记本
class Laptop(Computer):
    def __init__(self,cpu,memory,disc,weight):
        print('Laptop is inited')
        Computer.__init__(self,cpu,memory,disc)
        self.weight = weight
    def outputConfig(self):
        print('Cpu:{},Memory:{},DIsc:{},Weight:{}'.format(self.cpu,self.memory,self.disc,self.weight))

my_laptop = Laptop('CoreI7','8g','256g','1.3kg')
my_laptop.outputConfig()

# 平板
class Plant(Computer):
     def __init__(self,cpu,memory,disc,operate_system):
        print('Plant is inited')
        Computer.__init__(self,cpu,memory,disc)
        self.operate_system = operate_system
     def outputConfig(self):
        print('Cpu:{},Memory:{},DIsc:{},Operate_System:{}'.format(self.cpu,self.memory,self.disc,self.operate_system))
my_ipad = Plant('A12','8g','256g','ios13')
my_ipad.outputConfig()

class Surface(Laptop,Plant):
    def __init__(self,cpu,memory,disc,operate_system,weight):
        print('Surface is inited')
        Laptop.__init__(self,cpu,memory,disc,weight)
        Plant.__init__(self,cpu,memory,disc,operate_system)
    def outputConfig(self):
        print('Cpu:{},Memory:{},DIsc:{},Operate_System:{},weight:{}'.format(self.cpu,self.memory,self.disc,self.operate_system,self.weight))


sp4 = Surface('Cire i5','4g','128g','win 10','908g')
sp4.outputConfig()