import unittest

from . import solutions


class TestSolutions(unittest.TestCase):

    def test_maze_step(self):
        maze = solutions.Maze("0\n0")

        maze.step()

        self.assertEqual(maze.current_pos, 0)


    def test_maze_end(self):
        maze = solutions.Maze("2\n0")

        with self.assertRaises(StopIteration):
            maze.step()


    def test_maze_count_steps(self):
        maze = solutions.Maze("0\n0")

        maze.step()

        self.assertEqual(maze.total_steps, 1)


    def test_maze_instruction_incremented(self):
        maze = solutions.Maze("0\n0")

        maze.step()

        self.assertEqual(maze.layout[0], 1)


    def test_maze_navigate(self):
        maze = solutions.Maze("0\n3\n0\n1\n-3")

        maze.navigate()

        self.assertEqual(maze.total_steps, 5)


    def test_puzzle_solution_1(self):
        maze = solutions.Maze(solutions.PUZZLE_INPUT)

        maze.navigate()

        self.assertEqual(maze.total_steps, 351282)


    def test_maze_with_weird_offset(self):
        maze = solutions.Maze("0\n3\n0\n1\n-3")
        maze.weird_offset = True

        maze.navigate()

        self.assertEqual(maze.total_steps, 10)


    @unittest.skip("Takes a long time to run")
    def test_puzzle_solution_2(self):
        maze = solutions.Maze(solutions.PUZZLE_INPUT)
        maze.weird_offset = True

        maze.navigate()

        self.assertEqual(maze.total_steps, 24568703)
