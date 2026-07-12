# asteroid-shooter
This is a simple "space invaders"-like game but you shoot asteroids with a rocket.

https://github.com/user-attachments/assets/4b3fe5ed-d854-4205-a9be-54d5d32586f3
# Features
- Score is tracked when a player shoots an asteroid
- (Public domain) Sound effects and background music
- Custom pixel art made by me
- Game gets slowly harder as player's score increases
- Title screen shows users controls and game over screen shows users their final score
# Installation
# Releases (Recommended)
Head over to [the releases page](https://github.com/nautrw/asteroid-shooter/releases/latest) and download the file for your operating system:
- Windows: `Asteroid_Shooter_Windows.exe` (A windows defender warning might pop up)
- Linux: `Asteroid_Shooter_Linux`
Simply execute the file and it should launch.
## Building From Scratch
**Minimum Python Version Required: Python 3.8**
1. Clone the GitHub repository onto your system
1. Open a shell inside the folder of the cloned repository
3. Copy and run the following commands:
- On Linux:

```shell
python -m venv .venv
.venv/scripts/activate
python -m pip install pyinstaller -r requirements.txt
python -m pyinstaller --onefile --windowed --add-data "assets/*:assets" --exclude-module numpy --exclude-module pandas --exclude-module scipy --exclude-module matplotlib --name="Asteroid Shooter" asteroid-shooter.py
```

- On Windows (Powershell):
```powershell
pip install pyinstaller -r requirements.txt
pyinstaller --onefile --windowed --add-data "assets\*;assets" --icon=assets/icons/icon.ico --exclude-module numpy --exclude-module pandas --exclude-module scipy --exclude-module matplotlib --name="Asteroid Shooter" asteroid-shooter.py
```

4. The executable should be in the `dist` folder:
- On Linux: `./dist/Asteroid\ Shooter`
- On Windows: `& '.\dist\Asteroid Shooter.exe'`

# How It Works
This project is a simple space invaders-like game where you shoot asteroids. This was built with Pygame (community edition). Every entity (player, asteroid, bullet) is its own class. All of them have their own update methods which are run. Depending on the nature of the entity, this could mean listening for user input and moving like the player, or just moving along the y-axis and checking if it will be out of bounds like the bullets and asteroids. The game is generally one big tight-knit bundle, as each update method requires its own arguments that are needed to check things or run functions.

# Libraries Used & Credits
- `pygame-ce` for graphics, user input, etc. (The main library of the project)
- `pyinstaller` for compiling the project
- Background music (public domain) by DST @ https://opengameart.org/content/tower-defense-theme
- Shooting sound (public domain) by farfadet46 @ https://opengameart.org/content/laser-fire-0