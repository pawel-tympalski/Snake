import random


class BlockGenerator:

    @staticmethod
    def generate_block(snake,board):
        x = 0
        y = 0
        additional_value = 10
        step = 10
        check = True
        while check:
            x = random.randrange(board.translation_polygon + board.polygon_width + additional_value,
                                 board.screen_width - board.translation_polygon - board.polygon_width - additional_value, step)
            y = random.randrange(board.translation_polygon + board.polygon_width + additional_value,
                                 board.screen_height - board.translation_polygon - board.polygon_width - additional_value, step)
            list_block = []
            list_segments = snake.get_list_segments()
            for segment in list_segments:
                if (segment.get_left_top_y() == y and segment.get_left_top_x() == x):
                    list_block.append(1)

            if len(list_block) == 0:
                check = False

        return x , y


