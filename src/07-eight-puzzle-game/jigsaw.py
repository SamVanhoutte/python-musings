from puzzle import Puzzle 
import random as rnd
from priority_queue import PriorityQ

class JigsawPlay:
    def __init__(self, board:Puzzle):
        self.__board = board

    def solve(self):
        puzzle = self.__board
        open_moves = PriorityQ() 
        closed_moves = set()
        taken_steps = {}

        # Adding current state of the puzzle with highest priority to the queue
        open_moves.put(puzzle.evaluate_manhattan(), puzzle)

        # As long as there are options to explore, we keep working.  
        # If we're out, the puzzle cannot be solved
        while (open_moves.get_depth() > 0): 
            # current move to evaluate
            locktoken, (cost, parent_move) = open_moves.peek()

            if(parent_move.completed()):
                print('Final state found !')
                return self.trace_back(taken_steps, parent_move.depth, puzzle.get_signature())

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
                
                current_cost = current_move.depth + current_move.evaluate_manhattan()
                current_signature = current_move.get_signature()
                if(current_signature in taken_steps.keys()):
                    print('already existing !!' , current_signature)
                else:
                    taken_steps[current_signature] = (move, parent_move.get_signature())
                open_moves.put(current_cost, current_move)

        return None

    def trace_back(self, taken_steps, depth, initial_state: str):
        trace = list()
        current_phase = '1234 5678:' + str(depth)  # the actual solution
        while (not(current_phase.startswith(initial_state))): #startswith to ignore depth
            #print('Tracing back', current_phase)
            trace.append(current_phase)
            current_phase = taken_steps[current_phase][1]
        trace.append(initial_state)
        return list(reversed(trace))

def main():
    puzz = Puzzle()
    puzz.set_state([[1, 2, 3],
                    [4, 7, 5],
                    [6, 8, 0]])
    puzz.set_state([[1, 2, 3],
                    [7, 5, 8],
                    [4, 6, 0]])
    print(puzz)
    jigsaw = JigsawPlay(puzz)
    steps = jigsaw.solve()
    #print(steps)
    for key in steps:
        print(Puzzle(key))

if __name__ == "__main__": main()