__author__ = "jacobvanthoog"

import wpilib

ROTATION_TICKS = 131072 # encoder ticks in a full rotation
COMPLETED_DISTANCE = 0.06
# when both motors are within this fraction of their full ticks
# the movement has completed

class Arm:
    
    def __init__(self, can):
        self.CAN = can
        self.CAN.reverseSensor(True)
        self.CAN.changeControlMode(wpilib.CANTalon.ControlMode.Position)
        self.CAN.setPID(1.0, 0.0002, 3.0, 0.0)

        # target position of the encoders
        self.CAN.setFeedbackDevice(wpilib.CANTalon.FeedbackDevice.QuadEncoder)
        #getPosition is updated more often than getEncPosition
        #but it is negative, because of reverseSensor()
        #TODO: try to remove negatives
        self.Target = -self.CAN.getPosition()
        self.zero()

        self.Velocity = 4000 # ticks per step

        
    
    # should be called once per loop!
    def update(self):
        self.rotateToPosition1(self.CAN, self.Target)
    
    def setTarget(self, position):
        self.Target = position + self.Zero
        print("Target set: ", position)
        
    def getTarget(self):
        return self.Target - self.Zero
    
    def moveTarget(self, amount):
        self.setTarget(self.getTarget() + amount)
    
    def getPosition(self):
        return -self.CAN.getPosition() - self.Zero
    
    def movePosition(self, amount):
        self.setTarget(self.getPosition() + amount)
    
    def zero(self):
        self.Zero = -self.CAN.getPosition()
    
    def movementCompleted(self, can, target):
        return abs(-self.CAN.getPosition() - target)\
            <= (COMPLETED_DISTANCE * ROTATION_TICKS)
    
    # DON'T USE THESE
    
    def rotateToPosition1(self, can, target):
        current = -can.getPosition()
        #if current == target:
            #print("At position")
            #can.set(current)
            #return(0)
        
        distance = (target - current) # amount motor should rotate
        
        value = 0
        if abs(distance) < self.Velocity:
            value = target
        else:
            if distance > 0:
                value = current + self.Velocity
            else:
                value = current - self.Velocity
        
        #print(current, target, distance, value)

        #TODO: try to remove this negative
        can.set(-value)
        return(distance)
    
    def rotateToPosition2(self, can, target):
        current = -can.getPosition()
        target = target
        if current == target:
            #print("At position")
            can.set(0)
            return(0)
        
        distance = target - current # amount motor should rotate
        
        if abs(distance) < (self.Velocity):
            pass
        else:
            if distance > 0:
                distance = self.Velocity
            else:
                distance = -self.Velocity
                
        #print(distance)
        
        can.set(-distance/2)
        return(distance)

