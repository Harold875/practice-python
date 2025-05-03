class R2Vector:
    
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(tuple(getattr(self,i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}'for key, val in vars(self).items()]
        args =  ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'
    
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i:getattr(self,i) + getattr(other,i) for i in vars(self)}
        return self.__class__(**kwargs)
    
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i:getattr(self,i) - getattr(other,i) for i in vars(self)}
        return self.__class__(**kwargs)
    
    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = { i:getattr(self, i) * other  for i in vars(self)}
            return self.__class__(**kwargs)
        elif type(self) == type(other):
            args = [ getattr(self, i) * getattr(other,i) for i in vars(self)]
            return sum(args)
        return NotImplemented
    
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self,i) == getattr(other,i) for i in vars(self))
            
    def __ne__(self, other):
        return not self == other        
                  
    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()
    
    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()  
    
    def __le__(self, other):
        return not self > other
    
    def __ge__(self, other):
        return not self < other
     
    def norm(self):
        return (sum(val**2 for val in vars(self).values()))**0.5
        


class R3Vector(R2Vector):
    
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
    
    # Formula producto vectorial R3
    # A . B = (ay * bz -  az * by), (az * bx - ax * bz), (ax * by -  ay * bx)
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': (self.y * other.z) - (self.z * other.y),
            'y': (self.z * other.x) - (self.x * other.z),
            'z': (self.x * other.y) - (self.y * other.x),
        }
        return self.__class__(**kwargs)

        

if __name__ == '__main__':
    # R2 Vector
    v1 = R2Vector(x=2, y=3)
    v2 = R2Vector(x=0.5,y=1.25)
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')
    print(f'v1 + v2 = {v1 + v2}')
    print(v1 == v2)


    # R3 Vector
    v11 = R3Vector(x=2, y=3, z=1)
    v12 = R3Vector(x=0.5,y=1.25, z= 2)
    v13 = v11.cross(v12)
    print(f'v11 x v12 = {v13}')
    print(f'v11 * v12 = {v11 * v12}')