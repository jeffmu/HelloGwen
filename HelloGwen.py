
# bash commands run at sudo level to get sense-hat working.
# /bin/sh
# sudo apt-get update
# sudo apt-get install sense-hat
# sudo reboot

# use sense_hat lib
from sense_hat import SenseHat

sense = SenseHat()

# use time 
from time import sleep

blue =  (0, 0, 255)
green = (0, 255,0)

for num in range(1,6):
    sense.show_letter(str(num),green)
    sleep (5)
