import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = list()
        for key,value in balls.items():
            for item in range(value):
                self.contents.append(key)

    def draw(self, balls):
        if balls > len(self.contents):
            draw_balls = self.contents.copy()
            self.contents.clear()
            return draw_balls
        draw_balls = random.sample(self.contents, balls)
        for ball in draw_balls:
            self.contents.remove(ball)
        
        return draw_balls 


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    expected_balls_list = list()
    for key,value in expected_balls.items():
            for item in range(value):
                expected_balls_list.append(key)
    
    M = 0
    N = num_experiments
    for experiment in range(num_experiments):
        hatcopy = copy.deepcopy(hat)
        drawn = hatcopy.draw(num_balls_drawn)
        flag = True

        for ball in expected_balls_list:
            if ball in drawn:
                drawn.remove(ball)
            else:
                flag = False
        if flag:
            M += 1

    return M/N



