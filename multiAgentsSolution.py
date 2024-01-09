
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):



  def getAction(self, gameState):
 
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

   
    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
   
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):

  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):


  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):


  def getAction(self, gameState):
 

class AlphaBetaAgent(MultiAgentSearchAgent):
 
  def getAction(self, gameState):


class ExpectimaxAgent(MultiAgentSearchAgent):


  def getAction(self, gameState):


def betterEvaluationFunction(currentGameState):


# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):


  def getAction(self, gameState):
 

