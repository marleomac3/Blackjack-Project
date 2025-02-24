# Blackjack-Project

This is a Blackjack Python project. The goal of this project is to create a simple blackjack game that can be played in the browser. 

The current file structure is as follows:

- `README.md`: This file, which provides an overview of the project and its contents.
- `requirements.txt`: A file that lists the dependencies required to run the project.
- `assets/`: A folder containing images and other assets used in the project.
- `database/`: A folder containing the database files used by the project.
- `game/`: A folder containing the game files used by the project.
- `gui/`: A folder containing the GUI files used by the project.
- `tests/`: A folder containing the test files used by the project.
- `main.py`: The main file of the project, which contains the main code for the project.

The project is currently in progress and is being worked on by myself w/ potential collaborators.

Here is a scope breakdown of the project components:

### Core Game Logic
- **`game/deck.py`:** Handles the creation, shuffling, and dealing of cards.
- **`game/player.py`:** Manages player and dealer actions.
- **`game/game_logic.py`:** Implements the rules of Blackjack.
- **`game/utils.py`:** Contains utility functions.

### Betting System
- **`game/betting.py`:** Handles betting logic and payouts.

### Game State Management
- **`game/game_state.py`:** Tracks the current state of the game.

### Database
- **`database/db_handler.py`:** Manages saving and loading game statistics.

### Testing
- **`tests/` folder:** Contains unit and integration tests for all components.

### GUI (Frontend)
- **`gui/blackjack_gui.py`:** Implements the graphical user interface using `tkinter`.

### Assets
- **`assets/` folder:** Stores static files like card images and fonts.

### Entry Point
- **`main.py`:** Initializes the game and starts the GUI.

### Setup (Using Bash)
- git clone https://github.com/marleomac3/Blackjack-Project.git
- cd Blackjack-Project
- python3 main.py