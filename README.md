# AI Search Algorithms Implementation

## Overview
This repository contains the implementation of various search algorithms to find the shortest path between two provincial centers in Iran. The project focuses on implementing the A* search algorithm and Breadth-First Search (BFS) algorithm to determine the optimal route with the minimum distance. The implementation includes data handling, heuristic calculations, and neighbor expansions to achieve efficient pathfinding.

## Features
- **"A-start Search Algorithm**
  - Utilizes heuristic-based search for efficient pathfinding.
  - Calculates the shortest path between two provincial centers.
  - Outputs the order of cities visited and the total distance.

- **Breadth-First Search (BFS) Algorithm**
  - Implements BFS for finding the shortest path in an unweighted graph.
  - Provides the path and distance between two cities.

## Files
- **`A_star.py`**: Contains the implementation of the A* search algorithm.
- **`BFS.py`**: Contains the implementation of the Breadth-First Search (BFS) algorithm.
- **`Adjacent_Cities.xlsx`**: Excel file listing the adjacency matrix for the provincial centers.
- **`Province_Center_Distance.xlsx`**: Excel file containing the direct distances between provincial centers.
- **`Heuristic_Distance.xlsx`**: Excel file containing heuristic distances for use in the A* algorithm.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- Libraries: pandas, openpyxl

You can install the required packages using the following command:
```bash
pip install pandas openpyxl
