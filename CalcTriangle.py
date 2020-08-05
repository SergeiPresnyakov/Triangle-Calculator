from math import acos
from math import degrees


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = a.distance_from(b)
        self.ac = a.distance_from(c)
        self.bc = b.distance_from(c)
        self.angle_A = None
        self.angle_B = None
        self.angle_C = None

    def is_triangle(self):
        return (
            self.ab < self.ac + self.bc and
            self.ac < self.ab + self.bc and
            self.bc < self.ab + self.ac
        )
    
    def calc_perimeter(self):
        return self.ab + self.ac + self.bc

    def calc_angles(self):
        self.angle_A = degrees(acos((self.ab ** 2 + self.ac ** 2 - self.bc ** 2) / (2 * self.ab * self.ac)))
        self.angle_B = degrees(acos((self.ab ** 2 + self.bc ** 2 - self.ac ** 2) / (2 * self.ab * self.bc)))
        self.angle_C = degrees(acos((self.bc ** 2 + self.ac ** 2 - self.ab ** 2) / (2 * self.bc * self.ac)))
    
    def area(self):
        p = self.calc_perimeter()
        return ((p / 2) * (p / 2 - self.bc) * (p / 2 - self.ac) * (p / 2 - self.ab)) ** 0.5

    def inner_circle_radius(self):
        p = self.calc_perimeter()
        return (((p / 2 - self.ab) * (p / 2 - self.ac) * (p / 2 - self.bc)) / (p / 2)) ** 0.5
    
    def outer_circle_radius(self):
        return (self.ab * self.ac * self.bc) / (4 * self.area())

    def median_len_sum(self):
        ma = 0.5 * (2 * (self.ab ** 2 + self.ac ** 2) - self.bc ** 2) ** 0.5
        mb = 0.5 * (2 * (self.bc ** 2 + self.ab ** 2) - self.ac ** 2) ** 0.5
        mc = 0.5 * (2 * (self.bc ** 2 + self.ac ** 2) - self.ab ** 2) ** 0.5
        return ma + mb + mc


def main():
    x_a = float(input())
    y_a = float(input())
    x_b = float(input())
    y_b = float(input())
    x_c = float(input())
    y_c = float(input())

    a = Point(x_a, y_a)
    b = Point(x_b, y_b)
    c = Point(x_c, y_c)
    tr = Triangle(a, b, c)

    if tr.is_triangle():
        tr.calc_angles()
        inner = round(tr.inner_circle_radius(), 4)
        outer = round(tr.outer_circle_radius(), 4)
        medians = round(tr.median_len_sum(), 4)
        print(f'{inner} {outer} {medians}')
    else:
        print('error')
    

if __name__ == '__main__':
	main()