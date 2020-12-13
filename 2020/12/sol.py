class Ferry:
    def __init__(self, direction = 'E'):
        self.direction = direction
        self.north = 0
        self.east = 0
        self.waypoint_north = 1
        self.waypoint_east = 10
        
    def reset_position(self):
        self.direction = direction
        self.north = 0
        self.east = 0
        
    def manhattan(self):
        return(abs(self.north)+abs(self.east))
        
    def position_updater(self, direction, distance):
        if direction == 'N':
            self.north += distance
        if direction == 'S':
            self.north -= distance
        if direction == 'E':
            self.east += distance
        if direction == 'W':
            self.east -= distance
    
    def direction_updater(self, direction, rotation):
        compass = {'N':0, 'E':90, 'S':180, 'W':270}
        compass_inv = {0:'N', 90:'E', 180:'S', 270:'W'}
        compass_dir = compass[direction]
        new_compass_dir = (compass_dir + rotation) % 360
        self.direction = compass_inv[new_compass_dir]

    def navigate(self, instruction):
        nav_key = instruction[0]
        nav_value = int(instruction[1:])
        if nav_key in ['N', 'S', 'E', 'W']:
            self.position_updater(nav_key, nav_value)
        if nav_key == 'F':
            self.position_updater(self.direction, nav_value)
        if nav_key in ['R', 'L']:
            sign = -1 if nav_key == 'L' else 1
            self.direction_updater(self.direction, sign*nav_value)
        

    def waypoint_position_updater(self, direction, distance):
        if direction == 'N':
            self.waypoint_north += distance
        if direction == 'S':
            self.waypoint_north -= distance
        if direction == 'E':
            self.waypoint_east += distance
        if direction == 'W':
            self.waypoint_east -= distance
            
    def waypoint_direction_updater(self, direction, rotation):
        north_diff = self.waypoint_north - self.north
        east_diff = self.waypoint_east - self.east
        
        rotations = {0: (north_diff, east_diff), 1: (-east_diff, north_diff),
                     2: (-north_diff, -east_diff), 3: (east_diff, -north_diff)}
        current_rotation_idx = [k for k,v in rotations.items() if rotations[k] == (north_diff, east_diff)][0]
        
        if direction == 'R':
            new_rotation = rotations[(rotation/90) % 4]
        if direction == 'L':
            new_rotation = rotations[4-((rotation/90) % 4)]
            
        self.waypoint_north = self.north + new_rotation[0]
        self.waypoint_east = self.east + new_rotation[1]

    def navigate_by_waypoint(self, instruction):
        nav_key = instruction[0]
        nav_value = int(instruction[1:])
        if nav_key in ['N', 'S', 'E', 'W']:
            self.waypoint_position_updater(nav_key, nav_value)
        if nav_key == 'F':
            north_diff = self.waypoint_north - self.north
            self.position_updater('N', nav_value*north_diff)
            east_diff = self.waypoint_east - self.east
            self.position_updater('E', nav_value*east_diff)
            self.waypoint_north = self.north + north_diff
            self.waypoint_east = self.east + east_diff
        
        if nav_key in ['R', 'L']:
            self.waypoint_direction_updater(nav_key, nav_value)
    
        
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from utils import load_input_as_list 

inp = load_input_as_list('input_day12.txt')
        
f = Ferry()

for i in inp:
    f.navigate(i)
    
print(f'Part one answer: {f.manhattan()}')
    
    

f = Ferry()

for i in inp:
    f.navigate_by_waypoint(i)
    
print(f'Part two answer: {f.manhattan()}')