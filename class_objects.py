class Robot:
    def __init__(self,name,version):
        self.name = name
        self.version = version
        self.internal_temperature = 20

    def greeting(self):
        print(f"Hello I'm {self.name}, Ready to help you!")

    def print_info(self):
        print(f"I'm {self.name}, my version is {self.version} and my internal temperature is {self.internal_temperature}")


my_robot = Robot("R2B2",2)
my_robot.print_info()