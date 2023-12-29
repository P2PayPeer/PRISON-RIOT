# cell.py
# Cell 
# Where the player resides most of their time, interacting with objects, engaging in personal activities, and receiving messages from ARIA or other characters. 
# Time spent: High

import random
import json

# Assuming we have a JSON structure to store and manage emotional states
emotional_state_json = '../CHAR/entities.json'  # Replace with actual path


# Cell Inventory & Function Index:
class Cell:
    def __init__(self):
        self.bed = Bed()
        self.toilet = Toilet()
        self.lockers = Lockers()
        self.exercise_equipment = ExerciseEquipment()
        self.reading_materials = ReadingMaterials()
        self.writing_supplies = WritingSupplies()
        self.light_switch = LightSwitch()
        self.door = Door()
        self.security_camera = SecurityCamera()
        self.microphone = Microphone()
        self.emergency_button = EmergencyButton()
        
    def interact_with_object(self, object_name):
        # Interaction logic based on the object
        if object_name == 'bed':
            self.bed.use()
        # Add other interactions for different objects


    def update_emotional_feedback(self, interaction_type, content=None):
        # Update emotional state based on the interaction
        emotional_state = self.load_emotional_state()

        # Logic to update the emotional state based on ARIA system
        if interaction_type == 'read':
            self.handle_desire(emotional_state, content)
        elif interaction_type == 'write':
            self.handle_anger(emotional_state, content)
        # Add other interaction types and corresponding emotional feedback

        self.save_emotional_state(emotional_state)


    def handle_desire(self, emotional_state, content):
        # Logic for Desire
        # Update emotional_state based on reading materials and writing supplies
        # ...
        pass

    def handle_anger(self, emotional_state, content):
        # Logic for Anger
        # Encourage expression of anger through writing, provide constructive feedback
        # ...
        pass

    # Add methods for handling Fear, Surprise, Joy, Anticipation, Trust, Sadness, Disgust

    # @staticmethod
    def load_emotional_state():
        # Load the current emotional state from JSON
        with open(emotional_state_json, 'r') as file:
            return json.load(file)


    # @staticmethod
    def save_emotional_state(emotional_state):
        # Save the updated state to JSON
        with open(emotional_state_json, 'w') as file:
            json.dump(emotional_state, file)

# Bed:  The standard issue bed is found in each prisoner's cell. 
#       It serves as a place to sleep or rest during downtime.
            
class Bed:
    def use(self):
        # Logic for using the bed
        update_emotional_state('rest')

# Toilet: A basic toilet facility located next to the bed. 
#       It allows prisoners to relieve themselves without leaving their cells.
        
class Toilet:
    def use(self):
        # Define functionalities of the toilet
        update_emotional_state('relieved')


# Sink: An overhead sink above the toilet area. 
#       Used for washing hands, faces, or other personal hygiene tasks. 
#       Water pressure may be limited.
        
class Sink:
    def use(self):
        # Define functionalities of the sink
        update_emotional_state('clean')


# Lockers: Two small lockers located near the entrance of the cell.
#       One locker contains personal belongings (clothing, shoes, etc.), 
#       while the other houses sanitary supplies (toothbrush, toothpaste, soap, shampoo). 
#       These lockers can be secured using numeric codes known only to the prisoner and staff members.
                
class Lockers:
    def use(self):
        # Define functionalities of the lockers
        update_emotional_state('sort')


# Exercise Equipment: A minimalist exercise set consisting of a pull-up bar and stationary bike.
#       This equipment helps prisoners maintain some level of fitness within their confined spaces.
        
class Exercise:
    def use(self):
        # Logic for exercising
        update_emotional_state('exercise')


# Reading Materials: A small selection of books and magazines provided by the prison library. 
#       These materials vary in content and quality, catering to different interests and reading levels.
        
class Reading:
    def read(self):
        # Logic for reading
        update_emotional_state('read')


# Writing Supplies: A pen and notepad placed on the bedside table. 
#       Prisoners use these to communicate with others, write letters, or engage in creative activities like journaling or writing stories.
        
class Writing:
    def write(self, content):
        # Analyze content for emotional cues
        update_emotional_state('write', content)

# Light Switch: Located on the wall near the door, the light switch controls the artificial lighting within the cell. 
#        There might be a dimmer function for adjusting light intensity during sleep or relaxation periods.
        
class Light:
    def use(self):
        # Define functionalities of the light switch
        update_emotional_state('alert')

# Door: Made of solid steel reinforced with security features such as cameras, microphones, and sensors. 
#       The door can only be opened by authorized personnel using special keys or remote access devices. 
#       Attempting to break down the door would result in immediate alarm activation and response from security personnel.
        
class Door:
    def use(self):
        # Define functionalities of the door
        update_emotional_state('anxious')

# Security Camera: A small camera mounted on the ceiling directly above the bed. 
#   Its primary purpose is to monitor prisoner activity within the cell for safety reasons;
#   however, it may also record any unauthorized actions taken by inmates.
        
class SecurityCamera:
    def use(self):
        # Define functionalities of the security camera
        update_emotional_state('watched')

# Microphone: Similar to the camera, a microphone is hidden within the cell ceiling. 
#       It picks up sounds inside the cell and transmits them to monitoring stations where guards can listen for potential issues or rule violations.
        
class Microphone:
    def use(self):
        # Define functionalities of the microphone
        update_emotional_state('monitored')

# Emergency Button: Located on the wall near the door, this button triggers an alarm signal when pressed. 
#       It is intended for use in cases of emergencies or serious threats to the prisoner's wellbeing. 
#       Abuse of this feature may result in disciplinary action.

class EmergencyButton:
    def use(self):
        # Define functionalities of the emergency button
        update_emotional_state('alert')



# While life within its confines is restrictive, the items and resources available offer prisoners ways to cope, adapt, and even thrive under these harsh conditions.

# The cell environment provides both functional necessities and opportunities for mental stimulation and personal growth.   
def update_emotional_state(interaction_type, content=None):
    # Update emotional state based on the interaction
    # Load the current emotional state
    with open(emotional_state_json, 'r') as file:
        emotional_state = json.load(file)

    # Logic to update the emotional state
    # ...

    # Save the updated state
    with open(emotional_state_json, 'w') as file:
        json.dump(emotional_state, file)

# Main game loop where the cell interactions would be processed
def game_loop():
    cell = Cell()
    # Game loop logic
