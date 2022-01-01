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
    #SERVO_ZERO_OFFSET = 0x66
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



# ------------------------------------------#
# Helper functions                          #
# ------------------------------------------#



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
#Initial position
theBoard.servoWrite(theBoard, motor_pin, 0)
      
# Create an infinite loop
while True:

    if pin_logo.is_touched():
        music.pitch(200, duration=150, wait=True)
        theBoard.servoWrite(theBoard, motor_pin, motor_angle)

    else:

        if button_a.is_pressed():

            music.pitch(200, duration=150, wait=True)

            # make sure we don't go above the motor limit!
            if motor_angle < 180:
                motor_angle+=step_angle

            # show the motor angle
            display.scroll("%d" %
                (motor_angle), delay=100, wait=True, loop=False)
            sleep(100)
    

        if button_b.is_pressed():

            music.pitch(200, duration=150, wait=True)

            # make sure we don't go above the motor limit!
            if motor_angle > 0:
                motor_angle-=step_angle

            # show the motor angle
            display.scroll("%d" %
                (motor_angle), delay=100, wait=True, loop=False)
            sleep(100)

    




    
