![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# Flappy Bird

https://github.com/0x414854/Flappy_Bird/assets/128352715/42d6cae7-9a11-4f2b-8f66-13ddb13d5f50

## **Description**
This Python project implements the classic **Flappy Bird game** using **Pygame**.
<br>Players can control a bird to fly through obstacles. The game keeps track of the player's score and logs it into a file with the player's name.


## **Features**
- **Collision Detection** : Detects collisions between the bird and the pipes or floor.
- **Dynamic Background** : Includes a dynamic background that moves as the bird flies.
- **Score Tracking** : Tracks the player's score and saves it to a file.
- **Sound Effects** : Includes sound effects for flapping, hitting, dying, and scoring points.
- **User Input** : Prompts the player to enter their name at the start of the game.
- **Automatic Directory Creation** : Creates a 'users' directory to store score files if it does not exist.

## **Prerequisites**
- **Python 3.x** installed on your machine
- **Pygame** library

## **Installation Instructions**
Make sure you have [Python](https://www.python.org/downloads/) and [Pygame](https://www.pygame.org/news) installed on your system.

1. Clone this repository to your machine.
   
   ```bash
   git clone https://github.com/0x414854/Flappy_Bird.git

2. Install the required libraries.

   ```bash
   pip install pygame

3. Once the installation is complete, you're ready to run the program!
   
   ```bash
   python3 flappyBird.py

## **Usage Examples**
- Run the Python script.
- Enter your name when prompted.
- Press the SPACE key to make the bird flap its wings.
- Avoid hitting the pipes and the ground.
- Your score will be displayed, and the final score will be saved in a text file in the 'users' directory.

## Tree Directory

Flappy_Bird/
<br>├── Assets/
<br>&nbsp;│ ├── bird-1.png
<br>&nbsp;│ ├── bird-2.png
<br>&nbsp;│ ├── angry-birds.png
<br>&nbsp;│ ├── bg_night_flappy_bird.png
<br>&nbsp;│ ├── floor.png
<br>&nbsp;│ ├── pipe.png
<br>&nbsp;│ ├── start_message.png
<br>&nbsp;│ ├── game_over_message.png
<br>&nbsp;│ └── Sounds/
<br>&nbsp;│ ├── sfx_wing.wav
<br>&nbsp;│ ├── sfx_hit.wav
<br>&nbsp;│ ├── sfx_die.wav
<br>&nbsp;│ └── sfx_point.wav
<br>├── flappy_bird.py
<br>└── README.md

## **License**
This project is licensed under the **MIT License**.

## **Author**
[**0x414854**](https://github.com/0x414854)
