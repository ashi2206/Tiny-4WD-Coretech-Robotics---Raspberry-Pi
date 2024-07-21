- 👋 Hi, I’m @ashi2206

This project controls a robot using a joystick. It interfaces with the Explorer HAT library to control the motors and uses the ApproxEng Input library to read joystick input.

Requirements

- Explorer HAT library 
- ApproxEng Input library
- Controller (PS3, PS4 or Equiv)
- Tiny 4WD CoreTech Robotics kit
- Rapberry Pi Zero WH

Installation and Usage

1. Install the required libraries:
   - If you are using the Explorer HAT for motor control, install the library using:
     ```bash
     pip install explorerhat
     ```
   - To read joystick input, install the ApproxEng Input library using:
     ```bash
     pip install approxeng.input
     ```

2. Connect the Explorer HAT:
   Ensure the Explorer HAT is connected to your robot's motors.

3. Run the script:
   Execute the script to start the robot controller.
   ```bash
   python robot_controller.py
   ```
4. Controller Instructions:
   Use the left joystick to control the robot's movement.
   Press the HOME button to stop the robot and exit the script.

