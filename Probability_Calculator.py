#Read Me
#This appliation simulates performing blindly grabbing balls from a hat
#simple examples of using copy, random and probability.
#Author: Kailee Lesko
#Version: 1.0

import copy
import random

#The hat object is what we are drawing balls in the experiment with.
class Hat:
    def __init__(self, **balls):
        self.contents = []
        for i in balls:
            for j in range(balls[i]):
                self.contents.append(i)

    def draw(self, amount):
        if amount > len(self.contents):
            hat_copy = copy.copy(self.contents)
            self.contents.clear()
            return hat_copy

        return [self.contents.pop(random.randrange(len(self.contents))) for i in range(0, amount)]

#m represents the "actual results" of the experiment.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0 #M is named after the instructions of the project
    for i in range(0, num_experiments):
        copiedhat = copy.deepcopy(hat)
        drawn = copiedhat.draw(num_balls_drawn)
        colors_correct = 0
        # for loop concept learned from @python learning on youtube
        # see source video here:https://youtu.be/ql_TvsW0kGo?si=S8zzOL9aw7HS2uSY
        for x in expected_balls.keys():
            if drawn.count(x) >= expected_balls[x]:
                colors_correct += 1
            if colors_correct == len(expected_balls):
                m += 1
    return m / num_experiments


if __name__ == '__main__':
    #sample experiment
    sample_hat = Hat(black=6, red=4, green=3)
    probability_exercise = experiment(sample_hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
    print(probability_exercise)