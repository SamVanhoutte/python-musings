from puzzle import Puzzle 
import random as rnd
from priority_queue import PriorityQ
from timeit import Timer
import matplotlib.pyplot as plt

class JigsawPlay:
    _board = None

    def __init__(self, board:Puzzle):
        self._board = board

    def solve(self, evaluation_method = 'good', return_steps: bool = True):
        puzzle = self._board
        open_moves = PriorityQ() 
        closed_moves = set()
        taken_steps = {}

        # Adding current state of the puzzle with highest priority to the queue
        open_moves.put(puzzle.evaluate(evaluation_method), puzzle)

        # As long as there are options to explore, we keep working.  
        # If we're out, the puzzle cannot be solved
        while (open_moves.get_depth() > 0): 
            # current move to evaluate
            locktoken, (cost, parent_move) = open_moves.peek()

            if(parent_move.depth > 50):
                print('Max depth of 50 reached, returning now')
                return None
            if(parent_move.completed()):
                # print('Final state found !')
                if (return_steps):
                    return self.trace_back(taken_steps, parent_move.depth, puzzle.get_signature())
                else:
                    return None

            open_moves.complete(locktoken)
            closed_moves.add(parent_move)

            for move in parent_move.get_available_moves():
                # Cloning the previous state and applying the available move
                current_move : Puzzle = parent_move.clone()
                current_move.move_cell(move[0], move[1])
                current_move.depth += 1 # increase cost
                
                # Ignore the actual state, if we've visited that already
                if (current_move in closed_moves):
                    continue
                
                current_cost = current_move.depth + current_move.evaluate(evaluation_method)
                current_signature = current_move.get_signature()
                if(not(current_signature in taken_steps.keys())):
                    taken_steps[current_signature] = (move, parent_move.get_signature())
                open_moves.put(current_cost, current_move)

        return None

    def trace_back(self, taken_steps, depth, initial_state: str):
        trace = list()
        current_phase = '1234 5678:' + str(depth)  # the actual solution
        while (not(current_phase.startswith(initial_state))): #startswith to ignore depth
            #print('Tracing back', current_phase)
            trace.append(current_phase)
            if(current_phase in taken_steps):
                current_phase = taken_steps[current_phase][1]
        trace.append(initial_state)
        return list(reversed(trace))

def time_solve_puzzle(evaluation_method:str, puzzles, print_steps: bool):
    print('Solving', len(puzzles), 'puzzles with the following evaluation method:', evaluation_method)
    for puzz in puzzles:
        jigsaw = JigsawPlay(puzz)
        jigsaw.solve(evaluation_method, print_steps)

def generate_puzzles(required_number:int):
    print('generating', required_number, 'puzzles')
    puzzles = []
    for _ in range(required_number):
        puzzles.append(Puzzle())
    return puzzles

def main():
    #First show one execution of a puzzle to solve
    pz = Puzzle('12375846 ')
    print('Solving the following puzzle and printing steps:')
    print(pz)
    jigsaw = JigsawPlay(pz)
    steps = jigsaw.solve('fair', True)
    for step in steps:
        print(Puzzle(step))

    #Now time everything and plot the graph
    number_executions = 10
    puzzles = generate_puzzles(number_executions)
    fair_lambda = Timer(lambda: time_solve_puzzle('fair', puzzles, False))
    fair_score = fair_lambda.timeit(number=1)
    weak_lambda = Timer(lambda: time_solve_puzzle('weak', puzzles, False))
    weak_score = weak_lambda.timeit(number=1)
    bad_lambda = Timer(lambda: time_solve_puzzle('bad', puzzles, False))
    bad_score = bad_lambda.timeit(number=1)
    good_lambda = Timer(lambda: time_solve_puzzle('good', puzzles, False))
    good_score = good_lambda.timeit(number=1)

    print ('Fair evaluation execution time: ', fair_score)
    print ('Weak evaluation execution time: ', weak_score)
    print ('Bad evaluation execution time: ', bad_score)
    print ('Good evaluation execution time: ', good_score)


    plt.plot(['bad', 'weak', 'fair', 'good'], [bad_score, weak_score, fair_score, good_score])
    plt.title('A* evaluation timing')
    plt.ylabel('Duration')
    plt.show()



if __name__ == "__main__": main()

