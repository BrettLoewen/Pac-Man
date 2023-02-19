### Purpose of Proof of Concepts

I used this to learn the basics of python and pygame. I experimented with the things I thought would be needed to recreate PacMan.

### Running

To run the proof of concepts, open the `App.py` file. Starting on line 32, which proof of concept runs is decided. Simply uncomment the one you want to run and comment out the rest. Then run `App.py` either from a terminal or using your editor's play button.

## Proof of Concepts:
- Input and Sprites:
	- Found in `InputPoC.py`
	- Demonstrates functionality relating to user input and sprite rendering
	- Features 2 sprites which can be moved independently using the WASD and arrow keys
	- One of the sprite has a looping animation that it plays
	- Both sprites rotate to face the direction they are currently moving in (limited to 90 degrees)
- Logging:
	- Found in `LoggerPoC.py`
	- Demonstrates the 2 primary types of logging found in `Logger.py` and how to customize their appearance
	- Demonstrates line drawing in the game window
	- Demonstrates console logging in the terminal
- File Management:
	- Found in `FilePoC.py`
	- Demonstrates reading from a text file
	- Demonstrates writing to a text file
	- Demonstrates reading from an image file
- Collision:
	- Found in `CollisionPoC.py`
	- Demonstrates how to detect whether or not 2 collider objects are overlapping
	- Has a visual log mode that can be enabled to show the overlaps

