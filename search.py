
import util

class SearchProblem:

  def getStartState(self):

     util.raiseNotDefined()
    
  def isGoalState(self, state):

     util.raiseNotDefined()

  def getSuccessors(self, state):

     util.raiseNotDefined()

  def getCostOfActions(self, actions):

     util.raiseNotDefined()
           

def tinyMazeSearch(problem):

  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):


def breadthFirstSearch(problem):
 
      
def uniformCostSearch(problem):


def nullHeuristic(state, problem=None):
 
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
 
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch