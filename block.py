import pygame


class Block:
    def __init__(self,x,y,board,color=(255,0,0)):
        self.block_start_x = x
        self.block_start_y = y
        self.board = board
        self.color = color

    def draw_block(self):
        block = pygame.draw.rect(self.board.get_screen(), self.color, (self.block_start_x,self.block_start_y , 10, 10), 0)
        pygame.display.update(block)

    def get_collision_point(self,direct):
        if direct == "E":
            x = self.block_start_x
            y = self.block_start_y + 5
            return (x, y)
        elif direct == "W":
            x = self.block_start_x + 10
            y = self.block_start_y + 5
            return (x, y)
        elif direct == "S":
            x = self.block_start_x + 5
            y = self.block_start_y
            return (x, y)

        elif direct == "N":
            x = self.block_start_x + 5
            y = self.block_start_y + 10
            return (x, y)

    def __str__(self):
        return "X = %d, Y = %d" % (self.block_start_x,self.block_start_y)