from puzzle import Puzzle 
import random as rnd
from priority_queue import PriorityQ

class JigsawPlay:
    def __init__(self, board:Puzzle):
        self.__board = board

    def solve(self):
        puzzle = self.__board
        open_moves = set([puzzle])
        closed_moves = set()
        taken_steps = {}

        # This will be the goal distance (g-score)
        moves_score = {puzzle.get_signature() : 0}
        # This will be the total cost function, which is the moves + heuristic evaluation (g+h)
        # no move cost, so only heuristic to start with the board
        cost_scores = {puzzle.get_signature() : puzzle.evaluate_manhattan()}  

        # As long as there are options to explore, we keep working.  
        # If we're out, the puzzle cannot be solved
        while (len(open_moves) != 0): 
            # current move to evaluate
            current_move : Puzzle = None

            for move in open_moves:
                if(current_move is None or cost_scores[move.get_signature()] < cost_scores[current_move.get_signature()]):
                    current_move = move

            if(current_move.completed()):
                print('Final state found !')
                print('g:',moves_score)
                print('f:',cost_scores)
                return taken_steps
            
            open_moves.remove(current_move)
            closed_moves.add(current_move)

            for move in current_move.get_available_moves():
                #print('Checking move', move)
                moved_state : Puzzle = current_move.clone()
                moved_state.move_cell(move[0], move[1])
                moved_state.depth += 1 # increase cost
                
                if (moved_state in closed_moves):
                    continue
                
                tentative_moves_score = 1
                if(current_move.get_signature() in moves_score):
                    tentative_moves_score = moves_score[current_move.get_signature()] + 1

                moved_signature = moved_state.get_signature()
                if(moved_state not in open_moves or tentative_moves_score < moves_score[moved_signature]):
                    #print('score (tent / score)', tentative_moves_score, moves_score[moved_state])
                    print('adding the move to the history')
                    taken_steps[move] = (current_move, 'direction')
                    #print(moved_state)
                    moves_score[moved_signature] = tentative_moves_score
                    cost_scores[moved_signature] = moves_score[moved_signature] + moved_state.evaluate_manhattan()
                    if(moved_state not in open_moves):
                        open_moves.add(moved_state)

        return None



def main():
    puzz = Puzzle()
    puzz.set_state([[1, 2, 3],
                    [4, 7, 5],
                    [6, 8, 0]])
    # puzz.set_state([[1, 2, 3],
    #                 [7, 5, 8],
    #                 [4, 6, 0]])
    print(puzz)
    jigsaw = JigsawPlay(puzz)
    steps = jigsaw.solve()
    for step in steps:
        print(step)

if __name__ == "__main__": main()