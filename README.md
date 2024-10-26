# Mystery Escape Room
### Welcome to Mystery Escape Room, a thrilling interactive escape room game built using Python, speech recognition, and text-to-speech technology! Your goal is to explore the room, solve clues, and escape, all while using voice commands to interact with the environment.

## Features
#### Voice Recognition: Use voice commands to interact with the game. The game listens to your commands and responds accordingly.
#### Text-to-Speech: The game speaks to you, guiding you through the room and responding to your actions.
#### Interactive Environment: Explore the room, find hidden objects, and solve puzzles to escape.
#### Graphical Interface: The game features a graphical user interface (GUI) with visual feedback based on your interactions.

## Technologies Used
#### Python: The core programming language used for the game.
#### SpeechRecognition: Python library for capturing and recognizing voice commands.
#### pyttsx3: Python text-to-speech conversion library.
#### Tkinter: GUI framework used for creating the game interface.
#### Pillow (PIL): Python Imaging Library used for image processing and displaying the background visuals.

## Installation
#### Clone the repository to your local machine
#### Copy code
#### git clone https://github.com/yourusername/mystery-escape-room.git
#### cd mystery-escape-room

## Install the required dependencies
#### Copy code and paste into terminal
> [!IMPORTANT]
pip install SpeechRecognition pyttsx3 Pillow
#### Ensure you have the required Google Speech API for speech recognition. You can also use another speech recognition API by modifying the code.

## Run the game
#### Copy code
#### python escape_room_game.py
#### How to Play
#### Launch the game: Start the game, and a window will open with instructions.
#### Interact with voice commands: Press the Speak button and give voice commands like:
#### "look around" to search the room.
#### "use flashlight" to interact with items.
#### "open door", "move rug", and more.
#### Solve puzzles: Follow the clues, solve puzzles, and escape from the room!

## Example Commands
#### "look around": Explore the room and get a description of what you see.
#### "move rug": Discover hidden objects under the rug.
#### "read note": Read a clue that helps you solve the puzzle.
#### "use key": Unlock the door and escape the room!

## Known Issues
#### Speech recognition errors: Background noise may interfere with speech recognition accuracy. Ensure you play in a quiet environment.
#### Timeout in listening: If you do not speak within 5 seconds, the listening will timeout. You can adjust the timeout in the code if needed.

## Contributions
Feel free to fork the repository, submit pull requests, or suggest features to enhance the game!

## License
#### This project is licensed under the MIT License. See the LICENSE file for more details.

