# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        """ 1 Para"""
        
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    movs = util.Stack()
    been = []
    first=(problem.getStartState(),'',0)
    movs.push(first)

    while not  movs.isEmpty():
        state = movs.pop()
        if problem.isGoalState(state[0]):
            acts = state[1].split(',')
            acts.pop(0)
            return acts
        if state[0] not in been:
            been.append(state[0])
            x = problem.getSuccessors(state[0])
            for s in x: movs.push((s[0],state[1]+','+s[1]))
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    movs = util.Queue()
    been = []
    acts= []
    first=(problem.getStartState(),'',0)
    movs.push(first)

    while not  movs.isEmpty():
        state = movs.pop()
        if problem.isGoalState(state[0]):
            acts = state[1].split(',')
            acts.pop(0)
            return acts
        if state[0] not in been:
            been.append(state[0])
            x = problem.getSuccessors(state[0])
            for s in x: movs.push((s[0],state[1]+','+s[1]))

def uniformCostSearch(problem):
    movs = util.Queue()
    been = []
    acts =[]
    first=(problem.getStartState(),'',0)
    movs.push(first)
    while not  movs.isEmpty():
        movs.list.sort(key=lambda x: x[2],reverse=True)
        state = movs.pop()
        if problem.isGoalState(state[0]):
            acts = state[1].split(',')
            acts.pop(0)
            return acts
        if state[0] not in been:
            been.append(state[0])
            x = problem.getSuccessors(state[0])
            sorted(x,key=lambda x: x[2],reverse=True)
            for s in x: 
                if s[0] not in been: movs.push((s[0],state[1]+','+s[1],state[2]+s[2]))
                    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
#BestFirst
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
