
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
yellow = (255,255,0)

color = yellow
colorBackground = blue

scroll_rate = .1

# command to show a letter
# sense.show_letter(str(num),green)

# command to show a line of text
# sense.show_message("Hello world!")

sense.clear()
sleep(1)
sense.show_message("Hello Gwen", text_colour=color, back_colour=colorBackground, scroll_speed=scroll_rate)

# for num in range(1,6):
#    sense.show_letter(str(num),green)
#    sleep (5)

sleep(15)
sense.clear()
