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
```
##Testing
You can test the program by modifying the move commands in the .in files or the ship positions in the .txt files. The game will behave differently depending on the inputs.

##Known Issues
- The program may not handle errors in input files correctly, such as misspelled filenames or incorrect move formats
- Some parts of the code, especially related to error detection, have not been thoroughly tested.

##Future Improvements
- Improve error handling for incorrect inputs.
- Refactor code to eliminate unnecessary complexity, such as the redundant letters list in the pull_OptionalShips() function.
- Add more robust testing to ensure all edge cases are handled.

### INSTRUCTIONS.md


# Battle of Ships - Instructions

## Game Overview
The goal of the game is to sink all of your opponent's ships before they sink yours. The game is played on a 10x10 grid where each player places their ships. Players then take turns firing shots at the opponent's grid, trying to hit and sink their ships.

## File Structure
- **Player1.txt / Player2.txt:** These files define the initial positions of the ships for each player. The grid is 10x10, with rows labeled 1-10 and columns labeled A-J.
- **Player1.in / Player2.in:** These files contain the move sequences for each player. Each move is represented as a coordinate (e.g., `5,E`), separated by semicolons.

## Ship Symbols
- `C` - Carrier
- `B` - Battleship
- `D` - Destroyer
- `S` - Submarine
- `P` - Patrol Boat

## Ship Placement
- Ships are placed on the grid using their first letter. For example, a Battleship might occupy `6,B;7,B;8,B;9,B`.
- The placement file must use semicolons (`;`) to separate ship parts and indicate empty spaces. For example: `C; ; ;D;D; ; ;S;S;S;`.

## How to Play
1. Place your ships on the grid by editing `Player1.txt` and `Player2.txt`.
2. Define your move sequence in `Player1.in` and `Player2.in`. Each move should be formatted as `Row,Column`, e.g., `5,E`.
3. Run the game by executing the command:
   ```bash
   python3 Assignment4.py "Player1.txt" "Player2.txt" "Player1.in" "Player2.in"
   ```
4.The game will display the board after each move, showing where ships have been hit or missed.

##Winning the Game
The game continues until one player has all their ships sunk. The game will automatically detect when a player has lost and declare the winner.

##Error Handling
- The game expects the input files to be correctly formatted. Any issues such as incorrect coordinates or missing files will result in an error message.
- It is recommended to test the game with different configurations to ensure that all possible scenarios are covered.

##Troubleshooting
- Ensure that all input files are in the correct directory.
- If the program crashes, check the format of your input files for any errors.

