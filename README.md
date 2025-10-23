# ICS2308_SCT212-0076_2023_BouricOkwaro_Ass1_Search_Pacman

**Student Name:** Bouric Okwaro  
**Registration Number:** SCT212-0076/2023  
**Course:** ICS2308 - Artificial Intelligence  
**Assignment:** Search Algorithms in Pacman

## Project Overview

This project implements various search algorithms for the classic Pacman game. The original codebase was written in Python 2 and has been successfully migrated to Python 3, ensuring compatibility with modern Python environments.

## Search Algorithms Implemented

The project includes implementation of several search algorithms:

1. **tinyMazeSearch** - A simple search algorithm for tiny mazes
2. **Breadth-First Search (BFS)** - Explores all nodes at the present depth before moving on to nodes at the next depth level
3. **Depth-First Search (DFS)** - Explores as far as possible along each branch before backtracking
4. **A* Search** - Uses a heuristic function to guide the search toward the goal efficiently

## Python 2 to Python 3 Migration

The original codebase was written in Python 2 and required significant updates to work with Python 3. The following changes were made:

### Syntax Updates

#### Print Statements
- **Before:** `print 'Average Score:', sum(scores) / float(len(scores))`
- **After:** `print('Average Score:', sum(scores) / float(len(scores)))`

#### Exception Handling
- **Before:** `except Exception, data:`
- **After:** `except Exception as data:`

#### File Operations
- **Before:** `file(fname, 'w')`
- **After:** `open(fname, 'w')`

#### Import Statements
- **Before:** `import cPickle`
- **After:** `import pickle as cPickle`

- **Before:** `import cStringIO`
- **After:** `import io`

- **Before:** `import Tkinter`
- **After:** `import tkinter as Tkinter`

### Tkinter GUI Updates

The graphics system required updates for Python 3 compatibility:
- Replaced deprecated `Tkinter.tkinter.dooneevent` calls with `update_idletasks()`
- Updated function signatures to remove deprecated parameters
- Fixed tkinter module references

### Game State Bug Fixes

Fixed the `GameState.__eq__()` method to properly handle `None` comparisons:
```python
def __eq__(self, other):
    if other is None:
        return False
    return self.data == other.data
```

### Grid Class Comparison Fix

Added `__lt__()` method to the Grid class to enable proper comparison in priority queues for A* search:
```python
def __lt__(self, other):
    """Less than comparison for priority queue compatibility"""
    if other is None:
        return False
    # Compare by converting to a tuple of tuples
    return tuple(tuple(row) for row in self.data) < tuple(tuple(row) for row in other.data)
```
This fix resolves TypeError issues when using A* search with food search problems.

## Files Modified

The migration involved updating the following files:
- `pacman.py` - Main game logic and search algorithms
- `util.py` - Utility functions and data structures
- `game.py` - Game state management and Grid class comparison fix
- `graphicsDisplay.py` - Graphics display system
- `graphicsUtils.py` - Graphics utilities and tkinter integration
- `textDisplay.py` - Text-based display system
- `search.py` - Search algorithm implementations
- `searchAgents.py` - Search agent and heuristic implementations

## Usage

To run the search algorithms, use the following command format:

```bash
python pacman.py -l [layout] -p SearchAgent -a fn=[search_function]
```

### Examples:

```bash
# Test with tiny maze
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

# Test BFS on medium maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Test DFS on medium maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

# Test A* search on medium maze
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar

# Test food search algorithms
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l tinySearch -p AStarFoodSearchAgent
python pacman.py -l smallSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent

# Run with quiet mode (no graphics)
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs -q
```

### Available Layouts:
- `tinyMaze` - Small 3x3 maze
- `smallMaze` - Small maze
- `mediumMaze` - Medium-sized maze
- `bigMaze` - Large maze
- `openMaze` - Open maze with fewer walls
- And many more in the `layouts/` directory

## Results

The search algorithms demonstrate different performance characteristics:

### Basic Search Algorithms
- **BFS**: Finds the shortest path but explores many nodes (269 nodes expanded, cost 68)
- **DFS**: Finds a path quickly but may not be optimal (146 nodes expanded, cost 130)
- **A***: Efficiently finds optimal path using heuristics (268 nodes expanded, cost 68)

### Food Search Performance
The food search algorithms show varying complexity:
- **tinySearch**: 27 steps, 2048 nodes expanded, 0.4 seconds
- **smallSearch**: 34 steps, 5660 nodes expanded, 2.1 seconds
- **testSearch**: 7 steps, 12 nodes expanded, 0.0 seconds
- **trickySearch**: 60 steps, 9481 nodes expanded, 3.7 seconds

**Note**: mediumSearch and bigSearch layouts are extremely complex and may take excessive time to complete. These are designed as challenging test cases for advanced heuristics.

## Technical Requirements

- Python 3.x
- tkinter (usually included with Python)
- No additional external dependencies required

## Troubleshooting

### Search Algorithms Hanging or Taking Too Long

Some layouts (particularly `mediumSearch` and `bigSearch`) are extremely complex and may take excessive time to complete. These layouts have many food pellets that create a large search space. 

**Solutions:**
1. Use the `-q` flag for quiet mode (text-only, no graphics)
2. Use the `--frameTime 0` flag to speed up visual display
3. Test with simpler layouts first (`testSearch`, `tinySearch`, `smallSearch`)
4. For complex layouts, consider using more efficient heuristics

**Recommended test order:**
1. Start with `testSearch` (7 steps, instant completion)
2. Try `tinySearch` (27 steps, ~0.4 seconds)
3. Test `smallSearch` (34 steps, ~2.1 seconds)
4. Use `trickySearch` for a moderate challenge (60 steps, ~3.7 seconds)
5. Only attempt `mediumSearch` and `bigSearch` if you need to test very complex scenarios

## Project Structure

```
ICS2308_SCT212-0076_2023_BouricOkwaro_Ass1_Search_Pacman/
├── pacman.py              # Main game and search algorithms
├── search.py              # Search algorithm implementations
├── searchAgents.py        # Search agent implementations
├── game.py                # Game state management
├── util.py                # Utility functions
├── graphicsDisplay.py     # Graphics display
├── graphicsUtils.py       # Graphics utilities
├── textDisplay.py         # Text display
├── layout.py              # Maze layout management
├── layouts/               # Pre-defined maze layouts
├── docs/                  # Documentation files
└── README.md             # This file
```

## Conclusion

This project successfully demonstrates the implementation of fundamental search algorithms in the context of pathfinding for the Pacman game. The Python 2 to Python 3 migration ensures the code remains maintainable and compatible with modern development environments. The search algorithms show clear differences in their approach to finding paths, with A* providing the best balance of optimality and efficiency when a good heuristic is available.