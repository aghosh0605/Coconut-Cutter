

# Coconut_Cutter-RUDRA

A trend going in South of India for making coconut cutter robot as it's difficult now a days to find a man to cut coconuts and in South there is too much coconut trees everywhere. So after our 1 months of hard work we finally did the prototype of the robot.


# Beaware of this

- Used Raspberry Pi4, Arduino to do the project.
- Tested On RPi4. Please connect Arduino with RPi before running the code.
- Don't change any file and folder name and dicrectories structure.
- Put all the files in Pi and run the python file named `codings/flask_app.py` with python3.
- Don't change Pi Camera ip address in `codings/index.html`
- You can change the flask webserver port also for hosting in `codings/flask_app.py`

### If you have all the components then follow `How to run :)` otherwise go with Docker Container at `docker_test Folder Documentation`.


# How to run :)

1. Pi setup

   - Install [**Motion camera**](https://programmaticponderings.com/2013/01/01/remote-motion-activated-web-based-video-surveillance-with-raspberry-pi/) and edit the configuration by `sudo nano /etc/motion/motion.conf` to get the camera feeds in webpage.
   - Install [**pyserial**](https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/) for serial cmmunication between Pi and Arduino. We are using USB(UART protocol) for communication.
   - Install Flask with Pip `pip3 install flask`
   - Install GPIO with pip `pip3 install gpio`
   - Go inside `coding` folder. We will be doing all here.
   - Serial folder contains Arduino code to upload in Arduino for serial Communication.
   - Keep the HTML file in **templates** otherwise you will get an error.
   - If you change HTML page name, be sure to change it also in python code also.
   - For further webpage development with different CSS, javascript, HTML file in flask [see this](https://exploreflask.com/en/latest/organizing.html)

2. Arduino Setup

   - Upload the Arduino code.
   - Connect the Arduino with Pi by USB

3. Run the python file by `python3 codings/flask_app.py`. Now, open the webpage with ip address and port number of Pi from any device within the Network and enjoy.


# docker_test Folder Documentation

This folder is created for those who has a compute module with **GPIO Pins** but don't have a Arduino or any microcontrollers or the real code under the coding folder 
isn't working.

Inside the **docker_test** folder run the commands. **docker_flask:v1** is the name of the image I choosed. You can choose anything.

- `sudo docker build -t docker_flask:v1 .` Build the docker image  
- `sudo docker images` Check if the docker image was created successfully
- `sudo docker run --privileged -p 8888:8888 docker_flask:v1` Run the docker image in a container with mapping inner port 8888 with outer port 8888
- `sudo docker container ls` Shows running docker containers
- `sudo docker stop <container id>` Stops the container that has the id. Find the container id with previous command.
- `sudo docker rmi --force docker_flask:v1` Force removes the docker image

# Modules Used

- Flask
- GPIO
- JQuery
- Docker

# Skills Used

- HTML5
- CSS Flex
- Javascript
- Python
- Arduino Language
- Network Basics

# Our team

1. Guides
   - Antariksh Bhaiya
   - Mayur Bhaiya
   - Lokesh Bhaiya
2. Team members

   - Mechanical:
     - Ayan
     - Sumit
   - Corporate:
     - Soumyadeep
     - Rahul
   - Electronics:
     - Aditya
     - Ashwin
   - Coding:
     - Aniruddha


