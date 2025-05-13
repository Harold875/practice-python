import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    __slots__ = ['__speed', '__height', '__angle']
    def __init__(self,speed, height, angle ):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
    
    def __str__(self):
        messaje = f'\n{self.__class__.__name__} details:\n'
        messaje += f'speed: {self.__speed} m/s\n'
        messaje += f'height: {self.__height} m\n'
        messaje += f'angle: {math.degrees(self.__angle):.0f}°\n'
        messaje += f'displacement: {self.__calculate_displacement():.1f} m\n'
        return messaje
        
    
    def __calculate_displacement(self):
        v = self.__speed
        h = self.__height
        g = GRAVITATIONAL_ACCELERATION
        cos = math.cos(self.__angle)
        sin = math.sin(self.__angle)
        d = v * cos * (v * sin + math.sqrt((v**2) * (sin**2) +  (2 * g * h))) / g
        return d
        


# test 
ball = Projectile(10, 3, 45)
print(ball)
# displacement_of_ball = ball._Projectile__calculate_displacement() # 12.6173996009878