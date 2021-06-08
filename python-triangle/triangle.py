#The sum of two side lengths of a triangle is always greater than the third side.
# If this is true for all three combinations of added side lengths, then you will have a triangle.[1]

def Triangle(x,y,z):
    #if x <= 0 or y <= 0 or z <= 0:
        #raise Exception("Sides can't be lower or equal to 0!")
    if x + y > z and x + z > y and y + z > x:
        if x == y and x == z:
            return "equilateral"
        if x == y or x == z or y == z:
            return "isosceles"
        else:
            return "scalene"
    else:
        raise Exception("TriangleError")

print(Triangle(2,2,-2))