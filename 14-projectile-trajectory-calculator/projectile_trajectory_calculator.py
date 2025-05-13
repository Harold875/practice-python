import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    __slots__ = ('__speed', '__height', '__angle')
    
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
    
    def __calculate_y_coordinate(self, x):
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x**2 / (
            2 * self.__speed**2 * math.cos(self.__angle)**2)
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate
    
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def height(self):
        return self.__height
    
    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @speed.setter
    def speed(self, new_value):
        self.__speed = new_value
        
    @height.setter
    def height(self, new_value):
        self.__height = new_value

    @angle.setter
    def angle(self, new_value):
        self.__angle = math.radians(new_value)

# test 
ball = Projectile(10, 3, 45)
print(ball)
coordinates = ball.calculate_all_coordinates()
print(ball.speed)
print(ball.angle)
# displacement_of_ball = ball._Projectile__calculate_displacement() # 12.6173996009878