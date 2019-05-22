import puzzle as pz 
import random as rnd
from priority_queue import PriorityQ

class JigsawPlay:
    def __init__(self, board:pz.puzzle):
        self.__board = board

    def solve(self):
        self.__board.depth = 0
        open_moves = PriorityQ()
        closed_moves = []

        current_state = self.__board.clone()
        previous_state : pz.puzzle = None

        open_moves.put(0, current_state) # (()(0, current_state))

        while open_moves.get_depth() > 0:
            locktoken, msg = open_moves.peek()
            board = msg[1]
            current_state = board.clone()
            current_state.depth += 1
            closed_moves.append(current_state.get_signature())

            if(current_state.completed()==True):
                return current_state

            for move_row, move_col in board.get_available_moves():
                next_move_state = current_state.clone()
                next_move_state.move_cell(move_row, move_col)
                if(next_move_state.get_signature() in closed_moves):
                    continue # already checked this
                next_move_state.depth += 1
                current_score = self.evaluate(current_state)
                if(previous_state==None or current_score < self.evaluate(previous_state)):
                    #if(previous_state!=None):
                    open_moves.put(current_score, current_state)
                previous_state = current_state
                #next_move_state.set

            open_moves.complete(locktoken)
            
        return None


    def a_star(self, goal, heuristic, output):
        closed_set = set()      
        open_set = set([self])
        came_from = {}
        
        g_score = {self : 0}
        f_score = {self : g_score[self] + heuristic(self,goal)}
        
        while (len(open_set) != 0):
#            print len(open_set),len(closed_set)
            current = None
            for node in open_set:
                if current is None or f_score[node] < f_score[current]:
                    current = node
            if current == goal:
                return output(self, came_from, current)
                
            open_set.remove(current)
            closed_set.add(current)
#             print "Closed set:"
#             for p in closed_set:
#                 print p
            for n in current.neighbors():
                neighbor = n[0]
#                 print "Neighbor:\n",neighbor
                if neighbor in closed_set:
#                     print "Current:\n",current
#                     print "Neighbor:\n",neighbor
                    continue
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = (current, n[1])
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor,goal)
                    if neighbor not in open_set:
                        open_set.add(neighbor)

        return "nil"



    def evaluate(self, board:pz.puzzle):
        if(board.completed()): 
            return 10
        else:
            return rnd.randint(0,9)