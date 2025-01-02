from Graphics import Circle
from Graphics.Rectangle import *
from Graphics.ThreeD_graphics import Cuboid
from Graphics.ThreeD_graphics.Sphere import area as sphere_area
from Graphics.ThreeD_graphics.Sphere import perimeter as sphere_perimeter

print(f"""Circle with Radius 5
Area: , {Circle.area(5)}
Perimeter: {Circle.perimeter(5)}
Rectangle with Length: 6, Breadth: 4
Area: {area(6, 4)}
Perimeter: {perimeter(6, 4)}
Sphere with Radius 4
Area: {sphere_area(4)}
Perimeter: {sphere_perimeter(4)}
Cuboid with Length: 6, Breadth: 4, Height: 3
Area: {Cuboid.area(6, 4, 3)}
Perimeter: {Cuboid.perimeter(6, 4, 3)}"""
)
