class Segment:
    def __init__(self,x,y, direction):
        self.left_top_x = x
        self.left_top_y = y
        self.left_bottom_x = x
        self.left_bottom_y = y + 10
        self.right_top_x = x + 10
        self.right_top_y = y
        self.right_bottom_x = x + 10
        self.right_bottom_y = y + 10
        self.list_direction = []
        self.list_direction.append(direction)

    def get_direction(self):
        return self.list_direction[0]

    def get_left_top_x(self):
        return self.left_top_x

    def set_left_top_x(self,value):
        self.left_top_x +=  value

    def get_left_top_y(self):
        return self.left_top_y

    def set_left_top_y(self, value):
        self.left_top_y += value

    def get_left_bottom_x(self):
        return self.left_bottom_x

    def set_left_bottom_x(self, value):
        self.left_bottom_x += value

    def get_left_bottom_y(self):
        return self.left_bottom_y

    def set_left_bottom_y(self, value):
        self.left_bottom_y +=  value

    def get_right_top_x(self):
        return self.right_top_x

    def set_right_top_x(self, value):
        self.right_top_x +=  value

    def get_right_top_y(self):
        return self.right_top_y

    def set_right_top_y(self, value):
        self.right_top_y += value

    def get_right_bottom_x(self):
        return self.right_bottom_x

    def set_right_bottom_x(self, value):
        self.right_bottom_x +=  value

    def get_right_bottom_y(self):
        return self.right_bottom_y

    def set_right_bottom_y(self, value):
        self.right_bottom_y +=  value

    def get_list_direction(self):
        return self.list_direction

    def set_list_direction(self, value):
        self.list_direction = value

    def __str__(self):
        return "left_top_x %d, left_top_y %d" % (self.get_left_top_x(), self.get_left_top_y())