import helpers.settings as settings
import helpers.helpers as helpers
import random

def wichteln():
    wichtelnMapping = {} # email(gifter) -> email(receiver)
    receiverList = settings.personsList.copy()
    for person in settings.personsList:
        if settings.DEBUG:
            print(f"looking for mapping for {person.email}.")
        foundMatch = False
        while not foundMatch:
            randomChoice = random.choice(receiverList)
            if randomChoice != person and randomChoice.email not in person.blacklist and randomChoice.relationship not in person.blacklist:
                if settings.DEBUG:
                    print(f"found mapping {person.email} to {randomChoice.email}.")
                wichtelnMapping[person.email] = randomChoice.email
                receiverList.remove(randomChoice)
                foundMatch = True
            if randomChoice.email == person.email:
                if settings.DEBUG:
                    print(f"Encountered collision while trying to map {person.email} to {randomChoice.email}. Reason: person mapped themselves.")
            if randomChoice.email in person.blacklist:
                if settings.DEBUG:
                    print(f"Encountered collision while trying to map {person.email} to {randomChoice.email}. Reason: {randomChoice.email} found in persons blacklist: {person.blacklist}")
            if randomChoice.relationship in person.blacklist:
                if settings.DEBUG:
                    print(f"Encountered collision while trying to map {person.email} to {randomChoice.email}. Reason: {randomChoice.relationship} found in persons blacklist: {person.blacklist}")
    return wichtelnMapping

settings.init()
helpers.read_persons_from_file()
mapping = wichteln()
print(mapping)