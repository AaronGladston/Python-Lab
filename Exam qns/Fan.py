class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,speed = SLOW,radius = 10,color ="blue",on = False):
        self.__speed = speed 
        self.__radius = radius
        self.__color = color
        self.__on = on
    def get_speed(self):
        return self.__speed
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    def get_on(self):
        return self.__on
    def set_speed(self,speed):
        self.__speed = speed 
    def set_radius(self,radius):
        self.__radius = radius
    def set_color(self,color):
        self.__color = color
    def set_on(self,on):
        self.__on = on

fan1 = Fan(Fan.FAST,10,"yellow",True)
fan2 = Fan(Fan.MEDIUM,5,"blue",False)

print(f"Fan1:-")
print(f"Speed = {fan1.get_speed()}")
print(f"On = {fan1.get_on()}")
print(f"Radius = {fan1.get_radius()}")
print(f"Color = {fan1.get_color()}")

print(f"\nFan2:-")
print(f"Speed = {fan2.get_speed()}")
print(f"On = {fan2.get_on()}")
print(f"Radius = {fan2.get_radius()}")
print(f"Color = {fan2.get_color()}")