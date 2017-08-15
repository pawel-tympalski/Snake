import pygame
from segment import Segment


class Snake:
    def __init__(self, startx, starty, board, color=(0,0,0)):
        self.start_x = startx
        self.start_y = starty
        self.board = board
        self.color = color
        self.list_segments = []
        segment = Segment(self.start_x, self.start_y, "E")
        self.list_segments.append(segment)

    def move(self):

        segments = self.get_list_segments()
        count = len(self.get_list_segments())
        for segment in segments:
            
            direction_list = segment.get_list_direction()

            current_direction = "NONE"

            if len(direction_list) == 1:
                current_direction = direction_list[0]

            elif len(direction_list) > 1:
                current_direction = direction_list.pop(0)

                segment.set_list_direction(direction_list)

            if current_direction == "E":
                move_x = 10

                old_x = segment.get_left_top_x()
                current_x = segment.get_left_top_x() + move_x

                if  current_x > (self.board.screen_width - self.board.translation_polygon - self.board.polygon_width):
                    out_of_border_x = old_x
                    current_x = self.board.translation_polygon + self.board.polygon_width

                    old_x = self.board.screen_width - self.board.translation_polygon - self.board.polygon_width - 10

                    segment.set_left_top_x(-(self.board.screen_width - self.board.polygon_width
                                             - self.board.polygon_width - self.board.translation_polygon
                                             - self.board.translation_polygon))

                    segment.set_left_bottom_x(-(self.board.screen_width - self.board.polygon_width
                                             - self.board.polygon_width - self.board.translation_polygon
                                             - self.board.translation_polygon))

                    segment.set_right_top_x(-(self.board.screen_width - self.board.polygon_width
                                             - self.board.polygon_width - self.board.translation_polygon
                                             - self.board.translation_polygon))

                    segment.set_right_bottom_x(-(self.board.screen_width - self.board.polygon_width
                                             - self.board.polygon_width - self.board.translation_polygon
                                             - self.board.translation_polygon))

                    pygame.draw.rect(self.board.get_screen(), self.color, (current_x, segment.get_left_top_y(), 10, 10),
                                     0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                     (old_x, segment.get_left_top_y(), 10, 10), 0)

                    pygame.draw.rect(self.board.get_screen(), self.board.border_color,
                                    (out_of_border_x, segment.get_left_top_y(), 10, 10), 0)

                else:
                    segment.set_left_top_x(move_x)
                    segment.set_left_bottom_x(move_x)
                    segment.set_right_top_x(move_x)
                    segment.set_right_bottom_x(move_x)


                    pygame.draw.rect(self.board.get_screen(), self.color, (current_x, segment.get_left_top_y(), 10, 10), 0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                 (old_x, segment.get_left_top_y(), 10, 10), 0)



            elif current_direction == "W":
                move_x = (-10)
                old_x = segment.get_left_top_x()
                current_x = segment.get_left_top_x() + move_x

                if current_x < (self.board.translation_polygon + self.board.polygon_width):

                    current_x = self.board.screen_width - self.board.polygon_width - self.board.translation_polygon - 10
                    out_of_border_x = current_x + 10
                    old_x = self.board.translation_polygon + self.board.polygon_width


                    segment.set_left_top_x(self.board.screen_width - self.board.translation_polygon - self.board.translation_polygon
                                           - self.board.polygon_width - self.board.polygon_width - 10)
                    segment.set_left_bottom_x(
                        self.board.screen_width - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width - 10)
                    segment.set_right_top_x(
                        self.board.screen_width - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width - 10)
                    segment.set_right_bottom_x(
                        self.board.screen_width - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width - 10)



                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(), (old_x , segment.get_left_top_y(), 10, 10),
                                     0)

                    pygame.draw.rect(self.board.get_screen(), self.color, (current_x, segment.get_left_top_y(), 10, 10),
                                 0)

                    pygame.draw.rect(self.board.get_screen(), self.board.border_color,
                                     (out_of_border_x, segment.get_left_top_y(), 10, 10), 0)

                else:
                    segment.set_left_top_x(move_x)
                    segment.set_left_bottom_x(move_x)
                    segment.set_right_top_x(move_x)
                    segment.set_right_bottom_x(move_x)
                    pygame.draw.rect(self.board.get_screen(), self.color, (current_x, segment.get_left_top_y(), 10, 10),
                                     0)

                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                (old_x, segment.get_left_top_y(), 10, 10), 0)


            elif current_direction == "N":
                move_y = (-10)
                old_y = segment.get_left_top_y()
                current_y = segment.get_left_top_y() + move_y

                if current_y < (self.board.polygon_width + self.board.translation_polygon):
                    current_y = self.board.screen_height - self.board.translation_polygon - self.board.polygon_width - 10
                    out_of_border_y = old_y - 10
                    old_y = self.board.polygon_width + self.board.translation_polygon

                    segment.set_left_top_y(self.board.screen_height - self.board.translation_polygon -
                                           self.board.translation_polygon - self.board.polygon_width - self.board.polygon_width - 10)

                    segment.set_left_bottom_y(self.board.screen_height - self.board.translation_polygon -
                                           self.board.translation_polygon - self.board.polygon_width - self.board.polygon_width - 10)

                    segment.set_right_top_y(self.board.screen_height - self.board.translation_polygon -
                                           self.board.translation_polygon - self.board.polygon_width - self.board.polygon_width - 10)

                    segment.set_right_bottom_y(self.board.screen_height - self.board.translation_polygon -
                                            self.board.translation_polygon - self.board.polygon_width - self.board.polygon_width - 10)

                    pygame.draw.rect(self.board.get_screen(), self.board.border_color,
                                     (out_of_border_y, segment.get_left_top_y(), 10, 10), 0)
                    pygame.draw.rect(self.board.get_screen(), self.color, (segment.get_left_top_x(), current_y, 10, 10),
                                     0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                     (segment.get_left_top_x(), old_y, 10, 10), 0)

                else:
                    segment.set_left_top_y(move_y)
                    segment.set_left_bottom_y(move_y)
                    segment.set_right_top_y(move_y)
                    segment.set_right_bottom_y(move_y)

                    pygame.draw.rect(self.board.get_screen(), self.color, (segment.get_left_top_x(), current_y, 10, 10), 0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                 (segment.get_left_top_x(), old_y, 10, 10), 0)


            elif current_direction == "S":
                move_y = 10
                old_y = segment.get_left_top_y()
                current_y = segment.get_left_top_y() + move_y

                if current_y > (self.board.screen_height - self.board.polygon_width - self.board.translation_polygon):
                    current_y = self.board.polygon_width + self.board.translation_polygon
                    out_of_border_y = old_y
                    old_y = self.board.screen_height - self.board.translation_polygon - self.board.polygon_width - 10

                    segment.set_left_top_y(-(
                        self.board.screen_height - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width ) )

                    segment.set_left_bottom_y(-(
                        self.board.screen_height - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width) )

                    segment.set_right_top_y(-(
                        self.board.screen_height - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width) )

                    segment.set_right_bottom_y(-(
                        self.board.screen_height - self.board.translation_polygon - self.board.translation_polygon
                        - self.board.polygon_width - self.board.polygon_width) )


                    pygame.draw.rect(self.board.get_screen(), self.color, (segment.get_left_top_x(), current_y, 10, 10),
                                     0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                     (segment.get_left_top_x(), old_y - 10, 10, 10), 0)

                    pygame.draw.rect(self.board.get_screen(), self.board.border_color,
                                     (segment.get_left_top_x(), out_of_border_y, 10, 10), 0)



                else:
                    segment.set_left_top_y(move_y)
                    segment.set_left_bottom_y(move_y)
                    segment.set_right_top_y(move_y)
                    segment.set_right_bottom_y(move_y)

                    pygame.draw.rect(self.board.get_screen(), self.color, (segment.get_left_top_x(), current_y, 10, 10), 0)
                    pygame.draw.rect(self.board.get_screen(), self.board.get_board_color(),
                                 (segment.get_left_top_x(), old_y, 10, 10), 0)


            pygame.display.flip()


    def get_head_x(self):
        return self.head_x

    def get_head_y(self):
        return self.head_y

    def add_segment(self):
        tail_segment = self.get_list_segments()[-1]
        direction = tail_segment.get_direction()
        if direction == "E":
            value = 10
            x = tail_segment.get_left_top_x() - value
            y = tail_segment.get_left_top_y()

            directions_from_tail_segment = tail_segment.get_list_direction()

            if len(directions_from_tail_segment) > 1:
                directions = []

                for d in directions_from_tail_segment:
                    directions.append(d)
                last_direction = directions[-1]
                directions[-1] = directions[-2]
                directions.append(last_direction)
                segment = Segment(x, y, direction)
                segment.set_list_direction(directions)
                self.list_segments.append(segment)
            else:

                segment = Segment(x,y, direction)
                self.list_segments.append(segment)

        elif direction == "W":
            value = 10
            x = tail_segment.get_left_top_x() + value
            y = tail_segment.get_left_top_y()

            directions_from_tail_segment = tail_segment.get_list_direction()

            if len(directions_from_tail_segment) > 1:
                directions = []

                for d in directions_from_tail_segment:
                    directions.append(d)
                last_direction = directions[-1]
                directions[-1] = directions[-2]
                directions.append(last_direction)
                segment = Segment(x, y, direction)
                segment.set_list_direction(directions)
                self.list_segments.append(segment)
            else:

                segment = Segment(x, y, direction)
                self.list_segments.append(segment)

        elif direction == "N":
            value = 10
            x = tail_segment.get_left_top_x()
            y = tail_segment.get_left_top_y() + value


            directions_from_tail_segment = tail_segment.get_list_direction()

            if len(directions_from_tail_segment) > 1:
                directions = []

                for d in directions_from_tail_segment:
                    directions.append(d)
                last_direction = directions[-1]
                directions[-1] = directions[-2]
                directions.append(last_direction)
                segment = Segment(x, y, direction)
                segment.set_list_direction(directions)
                self.list_segments.append(segment)
            else:

                segment = Segment(x, y, direction)
                self.list_segments.append(segment)

        elif direction == "S":
            value = 10
            x = tail_segment.get_left_top_x()
            y = tail_segment.get_left_top_y() - value


            directions_from_tail_segment = tail_segment.get_list_direction()

            if len(directions_from_tail_segment) > 1:
                directions = []

                for d in directions_from_tail_segment:
                    directions.append(d)
                last_direction = directions[-1]
                directions[-1] = directions[-2]
                directions.append(last_direction)
                segment = Segment(x, y, direction)
                segment.set_list_direction(directions)
                self.list_segments.append(segment)
            else:

                segment = Segment(x, y, direction)
                self.list_segments.append(segment)

    def get_list_segments(self):
        return self.list_segments

    def set_list_segments(self,i,segment):

        self.list_segments.pop(i)
        self.list_segments.insert(i, segment)

    def set_list_all_segments(self,segments):
        self.list_segments = segments
