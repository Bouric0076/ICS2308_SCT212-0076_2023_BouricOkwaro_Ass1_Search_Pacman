# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
  """
  "*** YOUR CODE HERE ***"
  # Initialize the stack with the start state and empty path
  stack = util.Stack()
  start_state = problem.getStartState()
  stack.push((start_state, []))
  
  # Keep track of visited states to avoid cycles
  visited = set()
  
  while not stack.isEmpty():
    current_state, path = stack.pop()
    
    # Check if we've reached the goal
    if problem.isGoalState(current_state):
      return path
    
    # Skip if we've already visited this state
    if current_state in visited:
      continue
    
    # Mark as visited
    visited.add(current_state)
    
    # Get successors and add them to the stack
    for successor, action, cost in problem.getSuccessors(current_state):
      if successor not in visited:
        new_path = path + [action]
        stack.push((successor, new_path))
  
  # Return empty list if no solution found
  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  # Initialize the queue with the start state and empty path
  queue = util.Queue()
  start_state = problem.getStartState()
  queue.push((start_state, []))
  
  # Keep track of visited states to avoid cycles
  visited = set()
  
  while not queue.isEmpty():
    current_state, path = queue.pop()
    
    # Check if we've reached the goal
    if problem.isGoalState(current_state):
      return path
    
    # Skip if we've already visited this state
    if current_state in visited:
      continue
    
    # Mark as visited
    visited.add(current_state)
    
    # Get successors and add them to the queue
    for successor, action, cost in problem.getSuccessors(current_state):
      if successor not in visited:
        new_path = path + [action]
        queue.push((successor, new_path))
  
  # Return empty list if no solution found
  return []
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  # Initialize the priority queue with the start state, empty path, and cost 0
  priority_queue = util.PriorityQueue()
  start_state = problem.getStartState()
  priority_queue.push((start_state, [], 0), 0)
  
  # Keep track of visited states to avoid cycles
  visited = set()
  
  while not priority_queue.isEmpty():
    current_state, path, cost = priority_queue.pop()
    
    # Check if we've reached the goal
    if problem.isGoalState(current_state):
      return path
    
    # Skip if we've already visited this state
    if current_state in visited:
      continue
    
    # Mark as visited
    visited.add(current_state)
    
    # Get successors and add them to the priority queue
    for successor, action, step_cost in problem.getSuccessors(current_state):
      if successor not in visited:
        new_path = path + [action]
        new_cost = cost + step_cost
        priority_queue.push((successor, new_path, new_cost), new_cost)
  
  # Return empty list if no solution found
  return []

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  # Initialize the priority queue with the start state, empty path, and cost 0
  priority_queue = util.PriorityQueue()
  start_state = problem.getStartState()
  priority_queue.push((start_state, [], 0), 0)
  
  # Keep track of visited states to avoid cycles
  visited = set()
  
  while not priority_queue.isEmpty():
    current_state, path, cost = priority_queue.pop()
    
    # Check if we've reached the goal
    if problem.isGoalState(current_state):
      return path
    
    # Skip if we've already visited this state
    if current_state in visited:
      continue
    
    # Mark as visited
    visited.add(current_state)
    
    # Get successors and add them to the priority queue
    for successor, action, step_cost in problem.getSuccessors(current_state):
      if successor not in visited:
        new_path = path + [action]
        new_cost = cost + step_cost
        # Calculate priority using cost + heuristic
        priority = new_cost + heuristic(successor, problem)
        priority_queue.push((successor, new_path, new_cost), priority)
  
  # Return empty list if no solution found
  return []
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
