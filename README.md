# Battle of Ships

This project is a command-line implementation of the classic Battleship game for two players. The game reads ship positions and move commands from input files, then simulates the battle by updating the game board and checking for victories.

## Features
- **Input Parsing:** The program reads ship positions from `Player1.txt` and `Player2.txt`, and move commands from `Player1.in` and `Player2.in`.
- **Game Logic:** The game updates the board after each move, checks if any ships have sunk, and determines if the game is over.
- **Output:** After each move, the current state of the game board is displayed, showing hits, misses, and the remaining ships.

## How to Run
To run the program, use the following command in your terminal:

```bash
python3 Assignment4.py "Player1.txt" "Player2.txt" "Player1.in" "Player2.in"
