import unittest
from Geometry import *


class MyTestCase(unittest.TestCase):
    def test_figure_name(self):
        shape = Shape()
        test = shape.figure_name()
        self.assertEqual(test, 'Figure')  # add assertion here

    def test_square_math_area(self):
        square = Square(1)
        square_area = square.area()
        self.assertEqual(square_area, 1)

    def test_square_math_perimeter(self):
        square = Square(1)
        square_perimeter = square.perimeter()
        self.assertEqual(square_perimeter, 4)

    def test_rectangle_math_area(self):
        rectangle = Rectangle(1, 2)
        rectangle_area = rectangle.area()
        self.assertEqual(rectangle_area, 2)

    def test_rectangle_math_perimeter(self):
        rectangle = Rectangle(1, 2)
        rectangle_perimeter = rectangle.perimeter()
        self.assertEqual(rectangle_perimeter, 6)

    def test_circle_math_area(self):
        circle = Circle(1)
        circle_area = circle.area()
        self.assertEqual(circle_area, 3.141592653589793)

    def test_circle_math_perimeter(self):
        circle = Circle(1)
        circle_perimeter = circle.perimeter()
        self.assertEqual(circle_perimeter, 6.283185307179586)

    def test_trapezoid_math_area(self):
        trapezoid = Trapezoid(1, 2, 1)
        trapezoid_area = trapezoid.area()
        self.assertEqual(trapezoid_area, 1.5)

    def test_trapezoid_math_perimeter(self):
        trapezoid = Trapezoid(1, 2, 1)
        trapezoid_perimeter = trapezoid.perimeter()
        self.assertEqual(trapezoid_perimeter, None)

    def test_rhombus_math_area(self):
        rhombus = Rhombus(2, 1)
        rhombus_area = rhombus.area()
        self.assertEqual(rhombus_area, 2)

    def test_rhombus_math_perimeter(self):
        rhombus = Rhombus(2, 1)
        rhombus_perimeter = rhombus.perimeter()
        self.assertEqual(rhombus_perimeter, 8)

    def test_triangle_math_area(self):
        triangle = Triangle(3, 4, 5)
        triangle_area = triangle.area()
        self.assertEqual(triangle_area, 6)

    def test_triangle_math_perimeter(self):
        triangle = Triangle(3, 4, 5)
        triangle_perimeter = triangle.perimeter()
        self.assertEqual(triangle_perimeter, 12)

    def test_triangle_math_semiperimeter(self):
        triangle = Triangle(3, 4, 5)
        triangle_semiperimeter = triangle.geron()
        self.assertEqual(triangle_semiperimeter, 6)

    def test_cube_math_area(self):
        cube = Cube(1)
        cube_area = cube.area()
        self.assertEqual(cube_area, 6)

    def test_cube_math_perimeter(self):
        cube = Cube(1)
        cube_perimeter = cube.perimeter()
        self.assertEqual(cube_perimeter, 12)

    def test_cube_math_volume(self):
        cube = Cube(1)
        cube_volume = cube.volume()
        self.assertEqual(cube_volume, 1)

    def test_parallelepiped_math_area(self):
        parallelepiped = Parallelepiped(1, 2, 3)
        parallelepiped_area = parallelepiped.area()
        self.assertEqual(parallelepiped_area, 22)

    def test_parallelepiped_math_perimeter(self):
        parallelepiped = Parallelepiped(1, 2, 3)
        parallelepiped_perimeter = parallelepiped.perimeter()
        self.assertEqual(parallelepiped_perimeter, 24)

    def test_parallelepiped_math_volume(self):
        parallelepiped = Parallelepiped(1, 2, 3)
        parallelepiped_volume = parallelepiped.volume()
        self.assertEqual(parallelepiped_volume, 6)

    def test_sphere_math_area(self):
        sphere = Sphere(1)
        sphere_area = sphere.area()
        self.assertEqual(sphere_area, 12.566370614359172)

    def test_sphere_math_volume(self):
        sphere = Sphere(1)
        sphere_volume = sphere.volume()
        self.assertEqual(sphere_volume, 4.1887902047863905)

    def test_cylinder_math_area(self):
        cylinder = Cylinder(1, 2)
        cylinder_area = cylinder.area()
        self.assertEqual(cylinder_area, 18.84955592153876)

    def test_cylinder_math_area_base(self):
        cylinder = Cylinder(1, 2)
        cylinder_area_base = cylinder.area_base()
        self.assertEqual(cylinder_area_base, 3.141592653589793)

    def test_cylinder_math_area_side(self):
        cylinder = Cylinder(1, 2)
        cylinder_side_area = cylinder.side_area()
        self.assertEqual(cylinder_side_area, 12.566370614359172)

    def test_cylinder_math_volume(self):
        cylinder = Cylinder(1, 2)
        cylinder_volume = cylinder.volume()
        self.assertEqual(cylinder_volume, 6.283185307179586)

    def test_cone_math_area(self):
        cone = Cone(1, 2)
        cone_area = cone.area()
        self.assertEqual(cone_area, 10.166407384630519)

    def test_cone_math_area_base(self):
        cone = Cone(1, 2)
        cone_area_base = cone.area_base()
        self.assertEqual(cone_area_base, 3.141592653589793)

    def test_cone_math_area_side(self):
        cone = Cone(1, 2)
        cone_side_area = cone.side_area()
        self.assertEqual(cone_side_area, 7.024814731040727)

    def test_cone_math_volume(self):
        cone = Cone(1, 2)
        cone_volume = cone.volume()
        self.assertEqual(cone_volume, 2.0943951023931953)

    def test_tripiramid_math_area(self):
        tripiramid = TriangularPyramid(3, 4, 5, 3)
        tripiramid_area = tripiramid.area()
        self.assertEqual(tripiramid_area, None)

    def test_tripiramid_math_area_base(self):
        tripiramid = TriangularPyramid(3, 4, 5, 3)
        tripiramid_area_base = tripiramid.area_base()
        self.assertEqual(tripiramid_area_base, 6)

    def test_tripiramid_math_side_area(self):
        tripiramid = TriangularPyramid(3, 4, 5, 3)
        tripiramid_side_area = tripiramid.side_area()
        self.assertEqual(tripiramid_side_area, None)

    def test_tripiramid_math_volume(self):
        tripiramid = TriangularPyramid(3, 4, 5, 3)
        tripiramid_volume = tripiramid.volume()
        self.assertEqual(tripiramid_volume, 6)


if __name__ == '__main__':
    unittest.main()
