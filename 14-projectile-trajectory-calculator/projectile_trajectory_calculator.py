import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"


class Projectile:
    __slots__ = ('__speed', '__height', '__angle')
    
    def __init__(self, speed, height, angle ):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
    
    def __str__(self):
        message = f'\n{self.__class__.__name__} details:\n'
        message += f'speed: {self.speed} m/s\n'
        message += f'height: {self.height} m\n'
        message += f'angle: {self.angle}°\n'
        message += f'displacement: {self.__calculate_displacement():.1f} m\n'
        return message
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})'
    
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


class Graph:
    __slots__ = ('__coordinates')
    
    def __init__(self, coord):
        self.__coordinates = coord
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__coordinates})'

    def create_coordinates_table(self):
        table = f'\n{"x":>3}{"y":>7}\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        
        return table

    def create_trajectory(self):
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]
        
        x_max, y_max = rounded_coords[0]
        for x, y in rounded_coords:
            x_max = x_max if x_max > x else x
            y_max = y_max if y_max > y else y
        
        matrix_list = [[" " for _ in range(x_max +  1)] for _ in range(y_max + 1)]
        
        for x, y in rounded_coords:
            matrix_list[-y-1][x] = PROJECTILE
        
        matrix = [''.join(row) for row in matrix_list]
        
        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        graph =  '\n'+ '\n'.join(matrix_axes) + '\n'

        
        return graph

# test 
ball = Projectile(10, 3, 45)
print(ball)
coordinates = ball.calculate_all_coordinates()
print(ball.speed)
print(ball.angle)
# displacement_of_ball = ball._Projectile__calculate_displacement() # 12.6173996009878
graph = Graph(coordinates)
# print(graph.create_coordinates_table())
print(graph.create_trajectory())

# for row in graph.create_trajectory():
#     print(row)