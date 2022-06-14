#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Program Purpose: Move the servomotor
# Author: Sam Hoh
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# ------------------------------------------#
# Imports                                   #
# ------------------------------------------#

from microbit import *
import math
import music

# ------------------------------------------#
# Create a class for the robotics board     #
# ------------------------------------------#

class KitronikRoboticsBoard:
    PRESCALE_REG = 0xFE
    MODE_1_REG = 0x00
    SRV_REG_BASE = 0x08
    MOT_REG_BASE = 0x28
    REG_OFFSET = 4
    #SERVO_MULTIPLIER = 226
    SERVO_MULTIPLIER = 190
    SERVO_ZERO_OFFSET = 0X66
    ANGLE_ZERO_OFFSET = 0

    chipAddress = 0x6C
    initialised = False
    stepInit = False
    stepStage = 0
    stepper1Steps = 200
    stepper2Steps = 200

    def __init(self):
            
        buf = bytearray(2)

        buf[0] = self.PRESCALE_REG
        buf[1] = 0x85 #50Hz
        i2c.write(self.chipAddress, buf, False)
        
        for blockReg in range(0xFA, 0xFE, 1):
            buf[0] = blockReg
            buf[1] = 0x00
            i2c.write(self.chipAddress, buf, False)

        buf[0] = self.MODE_1_REG
        buf[1] = 0x01
        i2c.write(self.chipAddress, buf, False)
        self.initialised = True

    def servoWrite(self, servo, degrees):
        if self.initialised is False:
            self.__init(self)
        buf = bytearray(2)
        calcServo = self.SRV_REG_BASE + ((servo - 1) * self.REG_OFFSET) #find the servo number
        # = 8 + ((servo number - 1) * 4)
        HighByte = False
        degrees+=self.ANGLE_ZERO_OFFSET
        PWMVal = ((degrees * 100 * self.SERVO_MULTIPLIER) / 10000) + self.SERVO_ZERO_OFFSET
        # (degree input * 100 * 266)/( 10000 + 102)

        if (PWMVal > 0xFF): #if PWMval more than 255
            HighByte = True
        buf[0] = calcServo
        buf[1] = int(PWMVal)
        i2c.write(self.chipAddress, buf, False)
        buf[0] = calcServo + 1
        if (HighByte):
            buf[1] = 0x01
        else:
            buf[1] = 0x00
        i2c.write(self.chipAddress, buf, False)

def loudness_to_level(sound_value):
    # give 10 levels of loudness
    return round(sound_value*(10)/256)

def how_hard_did_i_blow():
    # Play some sound 
    music.pitch(200, duration=150, wait=True)
    sleep(100)
    music.pitch(200, duration=150, wait=True)
    sleep(100)
    music.pitch(200, duration=150, wait=True)

    # Image display!
    display.show(Image.MUSIC_QUAVER)
    sleep(2000)

    # Recording
    loudness = loudness_to_level(microphone.sound_level())

    return loudness



# ------------------------------------------#
# Our main program                          #
# ------------------------------------------#


# Our variables

motor_angle = 0
step_angle = 10
motor_pin = 1

set_volume(100)

# Display an image on start-up so that we know the program loaded correctly
display.show(Image.GHOST)
sleep(2000)

# Create a class instance
theBoard = KitronikRoboticsBoard

# Initiate the microphone
target_angle = loudness_to_angle(microphone.sound_level())
      
# Create an infinite loop
while True:

    # This will reset it to zero!
    if pin_logo.is_touched():

        music.pitch(200, duration=150, wait=True)

        # Set motor angle to zero
        motor_angle = 0

        # show the motor angle
        display.scroll("%d" %
            (motor_angle), delay=100, wait=True, loop=False)
        sleep(100)

        # Tell the board to move the servomotor to motor_angle
        theBoard.servoWrite(theBoard, motor_pin, motor_angle)

    else:

        # Record sound
        if button_a.is_pressed():

            # Measure how hard you blow
            loudness = how_hard_did_i_blow
            motor_angle = 18*loudness

            # show the motor angle
            display.scroll(loudness, delay=100, wait=True, loop=False)
            sleep(100)

            # Tell the board to move the servomotor to motor_angle
            theBoard.servoWrite(theBoard, motor_pin, motor_angle)
    


    




    
