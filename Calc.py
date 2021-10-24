from Geometry import *


class GeometryCalc:
    figures = {
        1: 'Square',
        2: 'Rectangle',
        3: 'Trapezoid',
        4: 'Rhombus',
        5: 'Circle',
        6: 'Triangle',
        7: 'Cube',
        8: 'Parallelepiped',
        9: 'Sphere',
        10: 'TriangularPyramid',
        11: 'Cylinder',
        12: 'Cone'
    }
    Calc: bool = True
    calc_types = {}

    def display_figures(self):  # Display figures for user
        print("Figures:")
        for number, value in self.figures.items():
            print(number, ' - ', value)
        print()

    def get_figure(self):  # Getting figure from user
        self.display_figures()
        figure_number = 0
        while figure_number not in self.figures.keys():
            try:
                figure_number = int(input('Please enter figure number\n'))
            except ValueError:
                print('Incorrect value. Please, try again.')
                print()

        print(f'Your figure is {self.figures[figure_number]}')
        return figure_number

    def types_of_calculation(self):  # Display available types of calculation for user
        for number, value in self.calc_types.items():
            print(number, ' - ', value)

    def get_type_of_calculation(self):  # Get from user required calculation
        get_figure = self.variable_calculation()
        self.types_of_calculation()
        type_number = 0
        while type_number not in self.calc_types.keys():
            try:
                type_number = int(input('Please enter calculation number\n'))
            except ValueError:
                print('Incorrect value. Please, try again.')
                print()

        print(f'Your chosen calculation is {self.calc_types[type_number]}')
        return [get_figure, type_number]

    def variable_calculation(self):  # Get all calculation available for chosen figure
        get_figure = int(self.get_figure())
        if get_figure in range(1, 6):
            self.calc_types.update({
                1: 'area',
                2: 'perimeter'})

        elif get_figure == 6:
            self.calc_types.update({
                1: 'area',
                2: 'perimeter',
                3: 'semiperimeter'})

        elif get_figure in range(7, 9):
            self.calc_types.update({
                1: 'area',
                2: 'perimeter',
                3: 'volume'
            })
        elif get_figure == 9:
            self.calc_types.update({
                1: 'area',
                2: 'volume'
            })
        elif get_figure in range(10, 13):
            self.calc_types.update({
                1: 'area',
                2: 'perimeter',
                3: 'volume',
                4: 'area_base',
                5: 'area_side',
            })
        return get_figure

    @staticmethod
    def get_side_from_user(side: str):  # Get from user required sides
        while not isinstance(side, float):
            try:
                side = float(input(f'Enter {side} \n'))
            except ValueError:
                print('Incorrect value. Please, try again.')
                print()
        return side

    def asking_for_enter_side_or_radius(self, param: str):  # Method determines the required values
        if param == 'Circle' or param == 'Sphere':
            return self.get_side_from_user('radius')

        elif param == 'Square' or param == 'Cube':
            return self.get_side_from_user('side')

        elif param == 'Rectangle':
            side_length = self.get_side_from_user('length')
            side_width = self.get_side_from_user('width')
            return [side_length, side_width]

        elif param == 'Triangle':
            first_side = self.get_side_from_user('first side')
            second_side = self.get_side_from_user('second side')
            third_side = self.get_side_from_user('third side')
            return [first_side, second_side, third_side]

        elif param == 'Rhombus':
            height = self.get_side_from_user('height')
            base = self.get_side_from_user('base edge')
            return [base, height]

        elif param == 'Trapezoid':
            top_base = self.get_side_from_user('top base')
            bottom_base = self.get_side_from_user('bottom base')
            height = self.get_side_from_user('height')
            return [top_base, bottom_base, height]

        elif param == 'Parallelepiped':
            side_a = self.get_side_from_user('first edge')
            side_b = self.get_side_from_user('second edge')
            height = self.get_side_from_user('height')
            return [side_a, side_b, height]

        elif param == 'TrianglePyramid':
            first_side = self.get_side_from_user('base first side')
            second_side = self.get_side_from_user('base second side')
            third_side = self.get_side_from_user('base third side')
            height = self.get_side_from_user('height')
            return [first_side, second_side, third_side, height]

        elif param == 'Cylinder':
            radius = self.get_side_from_user('radius')
            height = self.get_side_from_user('height')
            return [radius, height]

        elif param == 'Cone':
            radius = self.get_side_from_user('radius')
            height = self.get_side_from_user('height')
            return [radius, height]

    def define_figure(self, figure: str):
        #  Method collects the object of the necessary figure
        if figure == 'Square':
            side = self.asking_for_enter_side_or_radius('Square')
            square = Square(side)
            return square

        elif figure == 'Cube':
            side = self.asking_for_enter_side_or_radius('Cube')
            cube = Cube(side)
            return cube

        elif figure == 'Circle':
            radius = self.asking_for_enter_side_or_radius('Circle')
            circle = Circle(radius)
            return circle

        elif figure == 'Sphere':
            radius = self.asking_for_enter_side_or_radius('Sphere')
            sphere = Sphere(radius)
            return sphere

        elif figure == 'Rectangle':
            [side_a, side_b] = self.asking_for_enter_side_or_radius('Rectangle')
            rectangle = Rectangle(side_a, side_b)
            return rectangle

        elif figure == 'Triangle':
            first_side, second_side, third_side = self.asking_for_enter_side_or_radius('Triangle')
            triangle = Triangle(first_side, second_side, third_side)
            return triangle

        elif figure == 'Rhombus':
            height, base = self.asking_for_enter_side_or_radius('Rhombus')
            rhombus = Rhombus(height, base)
            return rhombus

        elif figure == 'Trapezoid':
            [side_a, side_b, height] = self.asking_for_enter_side_or_radius('Trapezoid')
            trapezoid = Trapezoid(side_a, side_b, height)
            return trapezoid

        elif figure == 'Parallelepiped':
            [side_a, side_b, height] = self.asking_for_enter_side_or_radius('Parallelepiped')
            parallelepiped = Parallelepiped(side_a, side_b, height)
            return parallelepiped

        elif figure == 'TrianglePyramid':
            [first_side, second_side, third_side, height] = self.asking_for_enter_side_or_radius('Pyramid')
            pyramid = TriangularPyramid(first_side, second_side, third_side, height)
            return pyramid

        elif figure == 'Cylinder':
            [radius, height] = self.asking_for_enter_side_or_radius('Cylinder')
            cylinder = Cylinder(radius, height)
            return cylinder

        elif figure == 'Cone':
            [radius, height] = self.asking_for_enter_side_or_radius('Cone')
            cone = Cone(radius, height)
            return cone

        else:
            print("Not found figure")
            return 0

    def calculate(self):  # Main method in class
        f_num_calc_num = self.get_type_of_calculation()
        figure = self.define_figure(self.figures[f_num_calc_num[0]])
        if figure != 0:
            if self.calc_types[f_num_calc_num[1]] == 'area':
                print(f'Area of {figure.figure_name()} = {figure.area()}')
            elif self.calc_types[f_num_calc_num[1]] == 'perimeter':
                print(f'Area of {figure.figure_name()} = {figure.perimeter()}')
            elif self.calc_types[f_num_calc_num[1]] == 'semiperimeter':
                print(f'Area of {figure.figure_name()} = {figure.geron()}')
            elif self.calc_types[f_num_calc_num[1]] == 'volume':
                print(f'Area of {figure.figure_name()} = {figure.volume()}')
            elif self.calc_types[f_num_calc_num[1]] == 'side_area':
                print(f'Area of {figure.figure_name()} = {figure.side_area()}')
            elif self.calc_types[f_num_calc_num[1]] == 'base_area':
                print(f'Area of {figure.figure_name()} = {figure.area_base()}')
