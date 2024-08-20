# Python Projects

This repository contains Python scripts for a shopping list manager and a Tic-Tac-Toe game.

## Table of Contents

1. [Shopping List Manager](#shopping-list-manager)
   - [Features](#features)
   - [Usage](#usage)
   - [Requirements](#requirements)
   - [Installation](#installation)
   - [Running the Script](#running-the-script)
2. [Tic-Tac-Toe Game](#tic-tac-toe-game)
   - [Features](#features-1)
   - [Usage](#usage-1)
   - [Requirements](#requirements-1)
   - [Installation](#installation-1)
   - [Running the Script](#running-the-script-1)
3. [License](#license)

---

## Shopping List Manager

`shopping.py` is a Python script that allows users to manage their shopping list.

### Features

- Add items to the shopping list.
- Remove items from the shopping list.
- View the current shopping list.
- Save and load shopping lists.

### Usage

1. **Add Item**: You can add items to your shopping list by providing the name and quantity.
2. **Remove Item**: If you no longer need an item, you can remove it from your list.
3. **View List**: Display all items currently in your shopping list.
4. **Save and Load**: Save your shopping list to a file and load it when needed.

### Requirements

- Python 3.x

### Installation

No special installation is required. Just clone this repository and ensure you have Python 3.x installed.

```bash
git clone https://github.com/iiFadel/COE292.git
```
To run the shopping list manager, use the following command:

```bash
python shopping.py
```
When you run the script, you’ll be presented with a simple command-line interface where you can choose different options to manage your shopping list. The options typically include:

1. **Add an Item**:  
   - Select this option to add an item to your shopping list.
   - You will be prompted to enter the name of the item and the quantity you wish to add.
   - Example: If you want to add 2 apples, you would enter "apples" and "2" when prompted.

2. **Remove an Item**:  
   - Use this option to remove an item from your shopping list.
   - You will be prompted to enter the name of the item you want to remove.
   - The script will check if the item exists in your list and remove it if found.

3. **View Shopping List**:  
   - This option allows you to view all the items currently on your shopping list.
   - The script will display each item along with its quantity in a list format.

4. **Save Shopping List**:  
   - Select this option to save your current shopping list to a file.
   - The script will prompt you for a file name, and then save the list to that file for future use.

5. **Load Shopping List**:  
   - This option allows you to load a previously saved shopping list from a file.
   - You will be prompted to enter the name of the file you wish to load.
   - The shopping list from the file will be loaded and you can continue managing it.

6. **Exit**:  
   - This option exits the program.
   - Any unsaved changes to your shopping list will be lost, so make sure to save your list before exiting if needed.

After selecting an option, simply follow the prompts to complete the desired action. The script is designed to be user-friendly and guides you through each step with clear instructions.

## Tic-Tac-Toe Game

`tictactoe.py` is a Python script for a simple command-line Tic-Tac-Toe game.

### Features

- Play Tic-Tac-Toe against another player.
- Interactive command-line interface.
- Automatic detection of winning conditions.
- A grid-based board that updates with each move.
- Checks for a win, draw, or ongoing game after each move.

### Usage

1. **Start Game**:  
   - Run the script to start a new game of Tic-Tac-Toe.
   - The game is played between two players, with one player using "X" and the other "O".

2. **Make Moves**:  
   - The game board is displayed as a 3x3 grid with numbered positions.
   - Players take turns entering the number corresponding to the position where they want to place their mark (X or O).
   - Example: Entering "5" places your mark in the center of the grid.

3. **Determine Winner**:  
   - After each move, the script checks for a winning condition (three of the same marks in a row, column, or diagonal).
   - If a player wins, the game announces the winner and ends.
   - If all positions are filled without a winner, the game declares a draw.

4. **Replay or Exit**:  
   - After a game ends, players have the option to start a new game or exit.
   - Simply follow the prompts to play again or quit.

### Requirements

- Python 3.x

### Installation

No special installation is required. Just clone this repository and ensure you have Python 3.x installed.

```bash
git clone https://github.com/iiFadel/COE292.git
```
### Running the Script

To run the Tic-Tac-Toe game, use the following command:

```bash
python tictactoe.py
```
When you run the script, the game will present a 3x3 grid where players can take turns to place their marks (“X” or “O”). The positions on the grid are numbered from 1 to 9, corresponding to each cell. The game interface will guide the players through the following steps:

1. **Display the Game Board**:  
   - The game begins by displaying an empty grid:
     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```
   - Each number represents a position where a player can place their mark.

2. **Player Turns**:  
   - Player 1 starts by entering the number of the position where they want to place their "X".
   - The script updates the grid to show the move:
     ```
     X | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```
   - Player 2 then takes their turn by entering the number of the position for their "O".
   - The game continues with players alternating turns until a win or draw is determined.

3. **Winning Conditions**:  
   - After each move, the game checks for any winning condition:
     - Three marks in a row: Horizontally, vertically, or diagonally.
   - If a player wins, the game announces the winner and displays the final grid:
     ```
     X | X | X
     ---------
     4 | O | O
     ---------
     7 | 8 | 9
     ```
   - The game ends after a win, with the option to start a new game.

4. **Draw Condition**:  
   - If all positions are filled and no player has won, the game declares a draw.
   - Example of a drawn board:
     ```
     X | O | X
     ---------
     X | X | O
     ---------
     O | X | O
     ```
   - The script then asks if the players want to start a new game or exit.

5. **End Game or Replay**:  
   - After a game ends (either through a win or a draw), the script prompts the players to either replay or exit.
   - Players can choose to start a new game by following the prompts or close the script to quit.

The game provides a simple, interactive experience, allowing two players to enjoy a quick match of Tic-Tac-Toe directly in the terminal. The interface is user-friendly and ensures smooth gameplay by guiding players through each step.

---

## License

This project is licensed under the MIT License.
