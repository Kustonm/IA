# multiAgents.py
# --------------


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [
            ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # Buscamos la distacia minima a una comida
        minF = 9999.99
        for food in newFood.asList():
            dis = util.manhattanDistance(newPos, food)
            if dis < minF:
                minF = dis

        # Distancia minima al fantasma
        minG = 9999.99
        for ghost in newGhostStates:
            ghostP = ghost.getPosition()
            dis = util.manhattanDistance(newPos, ghostP)
            if dis < minG:
                minG = dis

        # Castigar estar cerca del fantasma y sumar estar cerca de comida o capsulas
        score = successorGameState.getScore()
        if minG <= 1:
            score -= 10
        score += 1 / (len(newFood.asList())+1)
        score += 10 / (len(successorGameState.getCapsules())+1)
        score += 1 / (minF+1)

        return score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        agent = 0

        def getValue(state, agent, depth):

            if state.isLose() or state.isWin() or depth == self.depth*state.getNumAgents():
                return (None, self.evaluationFunction(state))

            return minimax(state, agent, depth)

        def minimax(state, agent, depth):
            actions = state.getLegalActions(agent)
            nextAgent = (agent + 1) % state.getNumAgents()
            if agent != 0:
                bestScore = 1000000
                bestAction = None
                for action in actions:
                    successor = state.generateSuccessor(agent, action)
                    prev_score = bestScore
                    bestScore = min(bestScore, getValue(
                        successor, nextAgent, depth + 1)[1])
                    if bestScore != prev_score:
                        bestAction = action
                return (bestAction, bestScore)
            if agent == 0:
                bestScore = -1000000
                bestAction = None
                for action in actions:
                    successor = state.generateSuccessor(agent, action)
                    prev_score = bestScore
                    bestScore = max(bestScore, getValue(
                        successor, nextAgent, depth + 1)[1])
                    if bestScore != prev_score:
                        bestAction = action
                return (bestAction, bestScore)

        action, _ = getValue(gameState, agent, 0)
        return action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        agent = 0

        def getValue(state, agent, depth, alpha, beta):

            if state.isLose() or state.isWin() or depth == self.depth*state.getNumAgents():
                return (None, self.evaluationFunction(state))

            return minimax(state, agent, depth, alpha, beta)

        def minimax(state, agent, depth, alpha, beta):
            actions = state.getLegalActions(agent)
            nextAgent = (agent + 1) % state.getNumAgents()
            if agent != 0:
                bestScore = 1000000
                bestAction = None
                for action in actions:
                    successor = state.generateSuccessor(agent, action)
                    prev_score = bestScore
                    bestScore = min(bestScore, getValue(
                        successor, nextAgent, depth + 1, alpha, beta)[1])

                    if bestScore != prev_score:
                        bestAction = action

                    beta = min(beta, bestScore)

                    if alpha > beta:
                        return (bestAction, bestScore)

                return (bestAction, bestScore)

            if agent == 0:
                bestScore = -1000000
                bestAction = None
                for action in actions:
                    successor = state.generateSuccessor(agent, action)
                    prev_score = bestScore
                    bestScore = max(bestScore, getValue(
                        successor, nextAgent, depth + 1, alpha, beta)[1])

                    if bestScore != prev_score:
                        bestAction = action

                    alpha = max(alpha, bestScore)

                    if alpha > beta:
                        return (bestAction, bestScore)

                return (bestAction, bestScore)

        action, _ = getValue(gameState, agent, 0, -1000000, 1000000)
        return action


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        def expectimax(state, depth, agent):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), ''
            actions = state.getLegalActions(agent)
            if agent == 0:  # Pacman
                bestS = -9999.99
                bestA = ''
                for action in actions:
                    score = expectimax(state.generateSuccessor(
                        agent, action), depth, 1)[0]
                    if score > bestS:
                        bestS = score
                        bestA = action
                return bestS, bestA
            else:  # Fantasma
                if len(actions) == 0:
                    return self.evaluationFunction(state), ''
                scores = []
                for action in actions:
                    if agent == (gameState.getNumAgents()-1):
                        scores.append(expectimax(
                            state.generateSuccessor(agent, action), depth+1, 0)[0])
                    else:
                        scores.append(expectimax(state.generateSuccessor(
                            agent, action), depth, agent+1)[0])
                return sum(scores)/len(scores), ''
        return expectimax(gameState, 0, 0)[1]


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    currentPos = currentGameState.getPacmanPosition()
    currentFood = currentGameState.getFood()
    currentGhostStates = currentGameState.getGhostStates()
    currentScaredTimes = [
        ghostState.scaredTimer for ghostState in currentGhostStates]
    currentCapsules = currentGameState.getCapsules()

    ghostD = set()
    for ghost in currentGhostStates:
        ghostD.add(util.manhattanDistance(currentPos, ghost.getPosition()))
    minG = min(ghostD)
    ghostP = 0
    if minG <= 1:
        ghostP = -1000
    ghostP = -1000 if minG <= 1 else 0

    foodD = set()
    for food in currentFood.asList():
        foodD.add(util.manhattanDistance(currentPos, food))

    capsuleD = set()
    for capsule in currentCapsules:
        capsuleD.add(util.manhattanDistance(currentPos, capsule))

    foodR = 0
    if len(foodD) > 0:
        for dist in foodD:
            foodR += 10.0 / dist

    capsuleR = 0
    if len(capsuleD) > 0:
        for dist in capsuleD:
            capsuleR += 50.0/dist

    minF = 0
    if len(foodD):
        minF = min(foodD)
    foodP = 0
    if minF > 0:
        foodP = -10.0/minF

    ghostR = 0
    for state, scaredT in zip(currentGhostStates, currentScaredTimes):
        dist = util.manhattanDistance(currentPos, state.getPosition())
        if scaredT > 0:
            ghostR += 200 / dist

    score = currentGameState.getScore()+ghostP+foodR+capsuleR+foodP+ghostR

    return score


# Abbreviation
better = betterEvaluationFunction
