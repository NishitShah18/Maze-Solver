# Maze Solver

This project is a Python-based maze solver, developed as part of the DSA456 course assignment. The maze solver reads a maze from a text file and attempts to find a solution using a specified algorithm.

## Technologies Used:

- **Python 3.x**: The main programming language used for developing the maze solver.
- **File I/O**: For reading maze input from text files.
- **Pathfinding Algorithms**: The maze-solving logic may use algorithms such as depth-first search (DFS), breadth-first search (BFS), or others.

## Project Files:

- `a3_maze.py`: Main Python script that contains the maze-solving algorithm.
- `a3_maze1.txt`: Example text file containing a maze layout.
- `a3_maze2.txt`: Another example text file with a different maze layout.

## How to Run the Maze Solver:

1. Clone this repository or download the necessary files (`a3_maze.py`, and one or both of the maze text files: `a3_maze1.txt` or `a3_maze2.txt`).

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure you have Python 3 installed on your system. You can check by running:

   ```bash
   python3 --version
   ```

3. Run the maze solver using the following command:

   ```bash
   python3 a3_maze.py <maze_file>
   ```

   Replace `<maze_file>` with the path to the maze file (e.g., `a3_maze1.txt` or `a3_maze2.txt`).

   Example:

   ```bash
   python3 a3_maze.py a3_maze1.txt
   ```

4. The script will attempt to find a solution to the maze and display the result.

## Example Maze Layout:

The maze files (`a3_maze1.txt`, `a3_maze2.txt`) are structured as grids where:

- `#` represents walls.
- `S` represents the starting point.
- `E` represents the end/exit point.
- `.` represents open paths.

Example:

```
#########
#S.....E#
#...#...#
#########
```

## License:

This project is part of the DSA456 coursework and is not licensed for commercial use.
