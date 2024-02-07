# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


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


class SearchNode:
    """
    A node in the search tree. Contains a pointer to the parent (the node that
    this is a successor of) and to the actual state for this node. Note that if
    a state is arrived at by two paths, then there are two nodes with the same
    state.
    """

    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def getPath(self):
        # Returns the sequence of actions to go from the root to this node.
        actions = []
        current_node = self
        while current_node.parent is not None:
            actions.append(current_node.action)
            current_node = current_node.parent
        actions.reverse()  # The actions were added in reverse order, so reverse them to get the correct order.
        return actions


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


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

    # Initialize the fringe and visited set
    visited = set()
    fringe = util.Stack()

    start = problem.getStartState()
    start_node = SearchNode(start)
    fringe.push(start_node)

    # While there are nodes in the fringe
    while not fringe.isEmpty():
        # Pop the top node from the fringe
        current_node = fringe.pop()

        # If the current node is the goal, return the path
        if problem.isGoalState(current_node.state):
            return current_node.getPath()

        # If the current node has not been visited
        if current_node.state not in visited:
            # Add the current node to the visited set
            visited.add(current_node.state)

            # For each successor of the current node
            for successor, action, stepCost in problem.getSuccessors(current_node.state):
                # Create a new node for the successor
                new_node = SearchNode(successor, current_node, action, current_node.cost + stepCost)
                # Add the new node to the fringe
                fringe.push(new_node)

    # If the fringe is empty and no path is found, return an empty list
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Initialize the fringe and visited set
    visited = set()
    fringe = util.PriorityQueue()

    start = problem.getStartState()
    start_node = SearchNode(start)
    fringe.push(start_node, 0)

    # While there are nodes in the fringe
    while not fringe.isEmpty():
        # Pop the top node from the fringe
        current_node = fringe.pop()

        # If the current node is the goal, return the path
        if problem.isGoalState(current_node.state):
            return current_node.getPath()

        # If the current node has not been visited
        if current_node.state not in visited:
            # Add the current node to the visited set
            visited.add(current_node.state)

            # For each successor of the current node
            for successor, action, stepCost in problem.getSuccessors(current_node.state):
                # Create a new node for the successor
                new_node = SearchNode(successor, current_node, action, current_node.cost + stepCost)
                # Add the new node to the fringe
                fringe.push(new_node, len(new_node.getPath()))

    # If the fringe is empty and no path is found, return an empty list
    return []

def uniformCostSearch(problem):
    # Initialize the fringe and visited set
    visited = set()
    fringe = util.PriorityQueue()

    start = problem.getStartState()
    start_node = SearchNode(start)
    fringe.push(start_node, 0)

    # While there are nodes in the fringe
    while not fringe.isEmpty():
        # Pop the top node from the fringe
        current_node = fringe.pop()

        # If the current node is the goal, return the path
        if problem.isGoalState(current_node.state):
            return current_node.getPath()

        # If the current node has not been visited
        if current_node.state not in visited:
            # Add the current node to the visited set
            visited.add(current_node.state)

            # For each successor of the current node
            for successor, action, stepCost in problem.getSuccessors(current_node.state):
                # Create a new node for the successor
                new_node = SearchNode(successor, current_node, action, current_node.cost + stepCost)
                # Add the new node to the fringe
                fringe.push(new_node, new_node.cost)

    # If the fringe is empty and no path is found, return an empty list
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Initialize the fringe and visited set
    visited = set()
    fringe = util.PriorityQueue()

    start = problem.getStartState()
    start_node = SearchNode(start)
    fringe.push(start_node, 0)

    # While there are nodes in the fringe
    while not fringe.isEmpty():
        # Pop the top node from the fringe
        current_node = fringe.pop()

        # If the current node is the goal, return the path
        if problem.isGoalState(current_node.state):
            return current_node.getPath()

        # If the current node has not been visited
        if current_node.state not in visited:
            # Add the current node to the visited set
            visited.add(current_node.state)

            # For each successor of the current node
            for successor, action, stepCost in problem.getSuccessors(current_node.state):
                # Create a new node for the successor
                new_node = SearchNode(successor, current_node, action, current_node.cost + stepCost)
                # Add the new node to the fringe
                fringe.push(new_node, new_node.cost + heuristic(successor, problem))

    # If the fringe is empty and no path is found, return an empty list
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
