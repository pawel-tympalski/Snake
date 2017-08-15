import pygame
import time
from snake import Snake
from block import Block
import block_generator


class Board:
    def __init__(self, width, height,board_color):
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.board_color = board_color
        self.screen.fill(board_color)
        self.list_block = []
        self.score = 0
        self.translation_polygon = 40
        self.polygon_width = 20
        self.border_color = (255, 255, 255)
        self.pairs_direction =(("N","S"), ("E","W"))

        pygame.draw.polygon(self.screen, self.border_color, [(self.translation_polygon + self.polygon_width/2, self.translation_polygon + self.polygon_width/2),
                                                       (self.screen_width - self.translation_polygon - self.polygon_width/2, self.translation_polygon + self.polygon_width/2),
                                                       (self.screen_width - self.translation_polygon - self.polygon_width/2, self.screen_height - self.translation_polygon - self.polygon_width/2),
                                                       (self.translation_polygon + self.polygon_width/2, self.screen_height - self.translation_polygon - self.polygon_width/2)], self.polygon_width)
        pygame.display.flip()

    def get_score(self):
        return self.score

    def add_score(self,value):
        self.score += value

    def get_board_color(self):
        return self.board_color

    def get_list_block(self):
        return self.list_block


    def test_snake_collision(self,snake):

        collision = False

        segments = snake.get_list_segments()
        segment = segments[0]
        head_x = segment.get_left_top_x()
        head_y = segment.get_left_top_y()

        for i in range(1,len(segments)):
            segment = segments[i]
            current_x = segment.get_left_top_x()
            current_y = segment.get_left_top_y()

            if current_x == head_x and current_y == head_y:
                collision = True
                return collision

        return collision

    def test_collision(self,block, snake):

        head_segment = snake.list_segments[0]

        x_block_col, y_block_col = block.get_collision_point(head_segment.get_direction())
        head_segment_direct = head_segment.get_direction()

        if head_segment_direct == "E":
            x_head_col = head_segment.get_right_bottom_x()

            y_head_col = head_segment.get_right_bottom_y() - 5

            if y_block_col == y_head_col and x_head_col == x_block_col:

                snake.add_segment()
                self.add_score(1000)
                return True
            else:
                return False

        elif head_segment_direct == "W":

            x_head_col = head_segment.get_right_top_x()
            y_head_col = head_segment.get_right_bottom_y() - 5


            if y_block_col == y_head_col and x_head_col == x_block_col:

                snake.add_segment()
                self.add_score(1000)
                return True

            else:
                return False

        elif head_segment_direct == "N":
            x_head_col = head_segment.get_right_top_x() - 5
            y_head_col = head_segment.get_right_bottom_y()
            x_head_col2 = head_segment.get_right_top_x() - 5
            y_head_col2 = head_segment.get_right_top_y()

            if (y_block_col == y_head_col and x_head_col == x_block_col) or (y_block_col == y_head_col2 and x_head_col2 == x_block_col):

                snake.add_segment()
                self.add_score(1000)
                return True

            else:
                return False

        elif head_segment_direct == "S":
            x_head_col = head_segment.get_right_top_x() - 5
            y_head_col = head_segment.get_right_top_y()

            if y_block_col == y_head_col and x_head_col == x_block_col:

                snake.add_segment()
                self.add_score(1000)
                return True

            else:
                return False

    def play(self,start_x, start_y):

        directions = {"N": pygame.K_UP, "S": pygame.K_DOWN, "E": pygame.K_RIGHT, "W": pygame.K_LEFT}

        snake = Snake(start_x, start_y,self,(0,0,255))

        first_block = Block(300, 200,self)
        self.get_list_block().append(first_block)

        while True:

            snake.move()
            block_to_draw = self.get_list_block().pop(0)
            block_to_draw.draw_block()
            segments = snake.get_list_segments()
            seg = segments[0]
            current_direction = seg.get_list_direction()[0]

            time.sleep(0.4)

            game_over = self.test_snake_collision(snake)

            if game_over == True:
                return self.score

            directions_available = {}

            if current_direction == "W" or current_direction == "E":
                directions_available["S"] = pygame.K_DOWN
                directions_available["N"] = pygame.K_UP
            elif current_direction == "N" or current_direction == "S":
                directions_available["E"] = pygame.K_RIGHT
                directions_available["W"] = pygame.K_LEFT

            list_event = []
            for key in directions_available:
                list_event.append(directions_available[key])

            event = pygame.event.poll()

            exit_outcome = self.get_input(directions_available, event,list_event, snake)

            if exit_outcome is True:
                return self.score

            collision = self.test_collision(block_to_draw, snake)
            if collision is True:
                x, y = block_generator.BlockGenerator.generate_block(snake, self)
                new_block = Block(x, y, self)
                new_block.draw_block()
                self.list_block.append(new_block)

            else:
                self.list_block.append(block_to_draw)

    def iterate_snake(self,snake,i,key):

        snake_segments = snake.get_list_segments()

        for i in range(len(snake_segments)):
            if i == 0:
                segment = snake_segments[i]
                directions = segment.get_list_direction()
                directions[0] = key
                segment.set_list_direction(directions)

            else:
                previous_segment = snake_segments[i - 1]
                current_segment = snake_segments[i]

                directions_previous_segment = previous_segment.get_list_direction()
                directions_current_segment = current_segment.get_list_direction()


                current_pair = "NONE"

                for pair in self.pairs_direction:
                    if directions_current_segment[0] in pair:
                        current_pair = pair
                        break

                if key not in current_pair:


                    if directions_current_segment[-1] in current_pair:
                        for k in range(i - len(directions_current_segment)):
                            directions_current_segment.append(directions_current_segment[-1])
                        directions_current_segment.append(key)
                        current_segment.set_list_direction(directions_current_segment)

                    else:
                        for k in range( i - len(directions_current_segment)):
                            directions_current_segment.append(directions_current_segment[0])
                        directions_current_segment.append(key)
                        current_segment.set_list_direction(directions_current_segment)

                else:
                    for k in range( i - len(directions_current_segment)):
                        directions_current_segment.append(directions_current_segment[-1])
                    directions_current_segment.append(key)
                    current_segment.set_list_direction(directions_current_segment)

    def get_input(self, directions_available, event,list_event, snake):

            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key in list_event:
                    for key in directions_available:
                        if event.key == directions_available[key]:

                            list_segments = snake.get_list_segments()


                            if len(list_segments) == 1:
                                segment = list_segments[0]
                                directions = segment.get_list_direction()
                                directions.pop(0)
                                directions.append(key)
                                segment.set_list_direction(directions)

                            else:
                                i = 0
                                self.iterate_snake(snake, i, key)

                return False

    def get_screen(self):
        return self.screen





