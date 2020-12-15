class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        if height != None:
            self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
#method to define width of polygon
    def set_width(self, width):
        self.width = width
#method to define height of polygon
    def set_height(self, height):
        self.height = height
#method to return area of polygon
    def get_area(self):
        area = self.width*self.height
        return area
#method to return perimeter of polygon
    def get_perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter
#method to get length of diagonal of polygon
    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal
#method to display visual representation of polygon
    def get_picture(self):
        picture = ""
        if self.height >50 or self.width > 50:
            return "Too big for picture."
        for i in range(self.height):
            for i in range(self.width):
                picture += "*"
            picture += "\n"
        return picture
#method to check how many of a give shape can fit inside another
    def get_amount_inside(self, shape):
        area_1 = self.get_area()
        area_2 = shape.get_area()
        num_inside = area_1//area_2
        return num_inside

# specify a Square subclass
class Square(Rectangle):

    def __init__(self, width):
        self.width = width
        self.height = self.width

    def __str__(self):
        return "Square(side={})".format(self.width)
#method to change dimensions of the Square object
    def set_side(self, side):
        self.width = side
        self.height = side
