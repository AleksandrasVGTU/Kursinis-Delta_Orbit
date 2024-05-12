# Kursinis-Delta_Orbit



# ALL FILES IN MASTER BRANCH 
## What is your application?
Delta Orbit is a straightforward arcade-style game featuring a basic physics simulation of a rocket navigating through space. Player controls the rocket, aiming to survive for as long as possible while avoiding collisions with oncoming meteorites. The primary objective is to achieve the highest score possible.


## How to run the program?
1. Install python and pygame, to install pygame run
- `-m pip install -U pygame==2.5.2 --user`'
2. Download the Game Files: Download the zip file containing all the game code and graphic files.
3. Extract the Zip File: Extract the contents of the zip file to a location of your choice on your computer.
4. Launch Delta-Orbit.py: Navigate to the directory where you extracted the files and find the Delta-Orbit.py script. Double-click the script to launch the game.
5. Configure the Rocket: Use the arrow buttons on your keyboard to configure the rocket's parameters. Ensure that the values for delta mass and delta mass max are not negative or equal to 0.
6. Submit to Start the Game: Once you've configured the rocket to your liking, press the "Submit" button to start the game

  ## How to Use the Program

- **Controls:**
    - **W:** Increase the thrust vector.
    - **S:** Decrease the thrust vector.
    - **A:** Turn the thrust vector left.
    - **D:** Turn the thrust vector right.
    - **Z:** Set the thrust to maximum.
    - **X:** Set the thrust to zero.
  
- **Objectives:**
  - Navigate the rocket through space, avoiding collisions with oncoming meteorites.
  - Survive as long as possible to achieve the highest score.

- **Fail States:**
  - Colliding with a meteorite results in failure.
  - Touching the edge of the window also leads to failure.
  ## How the program covers (implements) functional requirements
   4 Pillars of OOP

1. **Encapsulation:** 
   - The program encapsulates related functionality within classes such as `Rocket`, `Meteor`, `ScoreManager`, and `GameObjectFactory`. Each class manages its own data and behavior, promoting modularity and code organization.

2. **Abstraction:**
   - Abstraction is achieved through the `Utils` module, which handles reading and writing JSON files without exposing the implementation details. Additionally, the `vector_to_coordinates` method in the `GameObject` class abstracts the calculation of vector coordinates.

3. **Inheritance:**
   - Inheritance is demonstrated through the `Rocket` and `Meteor` classes, both of which inherit from the `GameObject` class.

4. **Polymorphism:**
   - Polymorphism is showcased by the `GameObjectFactory` class, which implements the Factory pattern. By overriding the `create_game_object` method in subclasses like `MeteorFactory`.
  
   Design Patterns

1. **Singleton:**
   - The `Rocket` class utilizes the Singleton pattern to ensure that only one instance of the rocket object exists throughout the game. This pattern guarantees a single global state for the rocket object, preventing multiple instances from being created.

2. **Factory:**
   - The Factory pattern is implemented through the `GameObjectFactory` and `MeteorFactory` classes. By encapsulating the object creation process within factory classes, the program achieves loose coupling and flexibility in creating game objects.
  Reading and Writing from File

  - The program effectively reads and writes data from JSON files using the `Utils` module. This functionality allows for the customization of game parameters and persistence of game data between sessions.
  ## Challenges faced during the implementation
 - Variables for motion (stored as vecotor length and angle from oy axis).
 - Transformation of said Thrust and Speed vectors into X and Y coordinates for redering (this was achieved by using trigonometry).
 - Figuring out the Object Factory Method was a challenge as it was a new concept entierly.
 ## Conclusions
   The coursework involved developing a game called "Delta Orbit." Key findings include implementing a rocket simulation with features such as throttle control, gravity simulation, and collision detection with meteors. The program achieved a functional game loop with dynamic meteor spawning, user-controlled rocket movement, and scoring based on survival time. Additionally, it incorporated object-oriented design principles such as class inheritance and abstraction to manage game entities efficiently.
   ## How it would be possible to extend this application?
   - Add limited fuel system with fuel refilling pickups
   - New obstacles with different movement patterns
   - New mechanics like shooting the meteors to destroy them
   - Implement sounds effects and add animations
