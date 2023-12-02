from enum import Enum

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    ADDON = 3 # these are the partners of the children or their divorced parents
    FRIEND = 4
    OTHER = 5

def init():
    global Relation
    global personsFileDirectory
    global personsFile
    global personsList
    global DEBUG
    global subject
    global sender
    global senderEmail
    global password

    ####################
    ### Change these ###
    ####################
    personsFileDirectory = ''
    personsFile = 'persons.txt'
    subject = 'Ho Ho Ho'
    sender = ''
    senderEmail = ''
    password = '' # google app key

    ###########################
    ### Do NOT change these ###
    ###########################
    Relation = Enum('Relationship', ['PARENT', 'CHILD', 'ADDON', 'FRIEND', 'OTHER'])
    personsList = []
    DEBUG = True