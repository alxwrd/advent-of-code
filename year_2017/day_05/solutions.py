import os

with open(os.path.dirname(__file__) + "/input", "r") as f_:
    PUZZLE_INPUT = f_.read()


class Maze(object):

    def __init__(self, layout):
        self.layout = [int(line) for line in layout.splitlines()]
        self.current_pos = 0
        self.total_steps = 0


    def step(self):
        travel = self.layout[self.current_pos]
        self.layout[self.current_pos] += 1
        self.current_pos += travel
        self.total_steps += 1
        try:
            self.layout[self.current_pos]
        except IndexError:
            raise StopIteration


    def navigate(self):
        while True:
            try:
                self.step()
            except StopIteration:
                break
