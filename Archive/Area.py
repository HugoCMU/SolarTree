# Author: Hugo P.
# Project: https://github.com/HugoCMU/SolarTree
# Description: Area class defines area objects, which contain dictonaries
# of moves performed to reach and other information for that area

from brain import params
from Move import Move
import numpy as np
import string
import random
#import RGBHistogram
#import ORBFeatures

class Area:

    def __init__(self):

        # Initialize name for the area using random string of digits/characters
        self.name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

        # List of groups associated with the area
        self.groups = []

        # Initialize dictionary of pictures
        self.pics = {}

        # Initialize position of area (X, Y, Z, and Theta)
        self.pos = [0, 0, 0, 0]

        # Previous areas (creating a graph)
        self.previous = []

        # Dictionary of moves to get to this area from an origin area (key)
        # Length can be used to measure of strength of tie to previous area
        self.moves_performed = {}

    def distance_to_pos(self, given_pos):
        '''
            Returns distance from a given area to a given position
        '''

        # Exact Distance from given_pos to this pos
        diff = np.subtract(np.array(self.pos), np.array(given_pos))

        # Distance number is a weighted average
        distance = np.sum(
            np.multiply(params.p('DISTANCE_WEIGHT'), np.absolute(diff)))

        # returns tuple containing exact value, and just the distance number
        return (distance, diff)

    def distance_to_area(self, given_area):
        '''
            Returns distance between two given areas
        '''

        # Exact Distance from given_pos to this pos
        diff = np.subtract(np.array(self.pos), np.array(given_area.pos))

        # Distance number is a weighted average
        distance = np.sum(
            np.multiply(params.p('DISTANCE_WEIGHT'), np.absolute(diff)))

        # returns tuple containing exact value, and just the distance number
        return (distance, diff)

    def virutal_move(self, origin_area):
        '''
            Creates a virtual move from given origin area to a given target area
        '''

        # Create new move object
        move = Move()

        # Make sure move is set as a virtual move
        move.type = "Virtual"

        # Link areas together
        self.previous.append(area1)

        # Set initial and final positions of move
        move.initial_pos = origin_area.pos
        move.final_pos = self.pos

        # Get the direction vector for the move between the two areas
        move.direction_vector = [final - initial for final, initial in zip(move.final_pos[:-1], move.initial_pos[:-1])]

        # Fill in other fields in the virutal area
        move.getMotionPlan()

        # Add move to areas dictionary of moves
        self.moves_performed[origin_area.name] = move

    def describe(self):
        '''
            Prints out information about the room, such as list of areas, etc
        '''

        print "Area description: "
        print "     NAME: " + str(self.name)
        print "   GROUPS: " + str(self.groups)
        print "      POS: " + str(self.pos)
        print " PREVIOUS: " + str(self.previous)
