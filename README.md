# Simulation of Car Performance Using Physical Forces

## Overview
This Python application simulates the performance of cars under various conditions such as acceleration, maximum speed, braking, and traction force. It provides a user-friendly interface for users to either create their own car with custom parameters or choose from preset car configurations.

## Technical Details

### Modules

1. **Car Module (`car.py`):**
   - Defines a `Car` class with methods for calculating various aspects of car performance, such as acceleration, time to reach maximum speed, braking time, braking distance, and traction force.
   - Includes conversion functions for speed units and constants for typical decelerations on different road surfaces.

2. **BuildCar Module (`build_car.py`):**
   - Implements a GUI for entering car parameters and displaying results using the `customtkinter` library.
   - Provides options for users to input parameters such as brand, model, acceleration, maximum speed, and mass.
   - Calculates and displays car performance metrics based on user inputs, including acceleration, traction force, time to reach top speed, braking time, and braking distance.

3. **Menu Module (`menu.py`):**
   - Constructs the main menu interface with options to create a custom car or choose a preset car configuration.
   - Utilizes the `customtkinter` library to design buttons and labels for user interaction.

4. **Main Module (`main.py`):**
   - Integrates all modules to create the main application.
   - Sets up the root window, attaches the menu, and runs the event loop using the `customtkinter` library.

### GUI Components
- **CustomTkinter Library:**
  - Utilized for creating customized GUI components such as buttons, labels, frames, and entry fields.
  - Provides flexibility in design and layout for a visually appealing user interface.

### Execution Flow
- Upon execution, the application launches a main window with a menu.
- Users can choose to create their own car or select a preset car configuration.
- When creating a custom car, users input parameters such as brand, model, acceleration, maximum speed, and mass. The application then calculates and displays various performance metrics based on these inputs.
- Users can also select a preset car configuration, which may offer predefined parameters for popular car models.
- Performance metrics such as acceleration, traction force, time to reach top speed, braking time, and braking distance are displayed in the GUI for user reference.

## Dependencies
- `customtkinter`: A custom tkinter library for building graphical user interfaces in Python.
- `matplotlib`: Used for plotting graphs to visualize car performance metrics.

## Usage
- Ensure Python and the required dependencies are installed.
- Clone the repository and navigate to the project directory.
- Run the `main.py` script to launch the application.
- Follow the on-screen instructions to create a custom car or choose a preset configuration.

## Future Improvements
- Implement additional features such as comparing multiple cars, saving/loading car configurations, and optimizing the GUI for better user experience.
- Enhance error handling and input validation to provide more robust feedback to users.
