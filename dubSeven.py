from baseAgent import HBDagent
import random
import minimax

class dubSeven(HBDagent):
    def __init__(self):
        self.isChecked = False
        self.player = None
        self.enemy = None

    def step(self, state):
        '''
            Input:
                state - It's a 2D array of the entire board at the current time

            This function should return :
                x - the x coordinate on the board
                y - the y coordinate on the board
                quadrant - the quadrant that the user wants to rotate 
                            This is divided into 4 parts 
                            1 - board[:3, :3]
                            2 - board[:3, 3:]
                            3 - board[3:, :3]
                            4 - board[3:, 3:]
                direction -  this is the direction in which the quadrant should rotate in
                            1 - anticlockwise
                           -1 - clockwise
        '''

        if (not self.isChecked):
            for i in state:
                for j in i:
                    if (j == 1):
                        self.player = 2
                        self.enemy = 1
                    else:
                        self.player = 1
                        self.enemy = 2
            self.isChecked = True
        action = minimax.getBestAction(state.tolist(), 6, self.player, self.enemy)
        x, y = action.x_coordinate, action.y_coordinate
        if (action.square_index == 2):
            quadrant = 3
        elif (action.square_index == 3):
            quadrant = 2
        else:
            quadrant = action.square_index
        if (action.direction == 'L'):
            direction = 1
        else:
            direction = -1


        return [x, y, quadrant, direction]
