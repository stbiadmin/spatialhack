import RPi.GPIO as GPIO
import time, os, pygame

#Declare BCM pin 16 which is GPIO 23 of Raspberry Pi
sensor = 16

#Declare BCM pin 12 which is GPIO 18 of Raspberry Pi

led = 12

#Declare BCM pin 7 which is GPIO 4 of Raspberry Pi
motor = 7

###Declare the BCM mode of GPIO pins

GPIO.setmode(GPIO.BOARD)

###Setup individual pinouts

#set the behaviour of sensor as input
GPIO.setup(sensor,GPIO.IN)

#set the behaviour of led as output
GPIO.setup(led,GPIO.OUT)

#set the behaviour of motor as output
GPIO.setup(motor,GPIO.OUT)

##Setup pygame mixer (used to play sounds and music(
pygame.mixer.init()
#preload the sound into memory
sound = pygame.mixer.Sound('/home/justin/sonichack/spatialhack/media/567208__sergequadrado__announcement-sound.wav')

#infinite event loop driver code, stop on keyboard interrupt
try:
   timer_start = timer_end = 0
   while True:
      if GPIO.input(sensor):
         GPIO.output(led,False)
         GPIO.output(motor, False)
         sound.stop()
         time.sleep(.2)
         timer_start = time.time()
      else:
         print("Motion Detected! Turning on light! Firing up the motor!")
         GPIO.output(led,True)
         GPIO.output(motor,GPIO.HIGH)
         sound.play(-1)
         os.system('clear')
         
except KeyboardInterrupt:
   GPIO.cleanup()
   
   
   
