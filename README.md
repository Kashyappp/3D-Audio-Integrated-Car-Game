# 3D Audio Project

# Overview
This project focuses on creating an immersive audio experience using 3D sound principles. The goal is to leverage Head-Related Transfer Functions (HRTFs) to simulate spatial audio cues that mimic real-world phenomena in a Car driving Game or Simulation.

# Usage of HRTFs
HRTFs are critical to our simulation, providing the necessary data to create a 3D audio effect. By incorporating HRTFs, we can simulate how sounds reach the listener's ears from any point in space, creating a realistic audio experience. We have used CIPIC HRTF database for the HRTF anlong with considering the azimuth angles relative to the listener.

# Sound Quality
We prioritize high-fidelity audio samples and accurate reproduction of sound characteristics. This ensures that the sound quality remains top-notch, giving the user an immersive experience.

 # Sound Choice
The sounds used in this project were carefully selected to enhance the user's immersive experience. They are representative of the environment we aim to simulate and provide meaningful auditory cues to the user. The sound is a Car Audio taken from a real-world environment. Based on the user studides for this project we opted not to add environmental sounds to it.

# 3D Sound Movement
The movement of sound is handled with precision, taking into consideration the velocity of moving objects in the simulation. As objects pass by the listener, the sound dynamically pans from one ear to the other, reflecting real-world movement. 

# Design Decisions for Perceptual Consideration

1. **Dynamic Volume Adjustment** As objects approach or move away from the listener, we dynamically adjust the volume to emulate real-world volume changes based on distance.

2. **Accurate Spatialness and Consistency** It is essential to make sure that the visual representation of the environment and the aural spatial signals are congruent when building a 3D sound environment. This implies that the sound should accurately depict the trajectory of any visual object, such as an enemy vehicle, that appears to be approaching the player from a particular angle. 

3. **Binaural Panning** Sound is not only panned between the left and right channels but is also processed with HRTFs to give the user a sense of verticality and depth, enhancing the realism of the audio.

# Installation and Setup
1. Clone the repository:
   ```
   git clone [repository-url]
   ```
2. Navigate to the project directory and set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

# Running the Application
With the virtual environment activated and dependencies installed, you can run the application using:
```
python main.py
```

# Contributing
We welcome contributions to this project. If you would like to contribute, please fork the repository and submit a pull request with your proposed changes.

# License
This project is licensed under the [LICENSE-type] License - see the LICENSE.md file for details.

x# Acknowledgements
- We thank the contributors who have provided the HRTF data sets used in this project.
- Special thanks to the pygame community for their support.
- Special Thanks to Our professor Dr.Kyla Mcmullen and Teaching Assistant Mr. Chensen Lu for guiding us about the 3D audio contents in this semester.

