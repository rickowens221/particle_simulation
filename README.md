# Particle Simulation with Slower Attraction

This is a simple particle simulation using Python and Pygame, where particles move chaotically around the screen and are attracted to the mouse cursor when the left mouse button is pressed. The attraction speed and particle velocity are adjustable, and friction slows particles over time.

## Features

- **Chaotic Motion**: Particles move randomly around the screen.
- **Mouse Attraction**: Particles are attracted to the cursor when the left mouse button is pressed.
- **Boundary Collisions**: Particles reflect off screen edges.
- **Adjustable Parameters**: Fine-tune the speed, friction, and randomness of particle movement.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/particle-simulation.git
   cd particle-simulation
    ```
Install Pygame:
 ```bash
pip install pygame
 ```
Usage
Run the simulation with:

 ```bash
python particle_simulation.py
 ```
Left Click: Hold the left mouse button to attract particles to the cursor.
Release Mouse: Particles continue their motion without attraction.

Modify these variables in particle_simulation.py to adjust the simulation:

num_particles: Number of particles in the simulation.
friction: Friction factor that slows down particle speed over time.
chaos_intensity: Intensity of chaotic motion when no attraction is applied.
force: Maximum attraction force applied when the cursor is held down.
