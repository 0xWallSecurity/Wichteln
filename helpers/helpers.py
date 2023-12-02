import helpers.settings as settings
import classes.Person as Person
import os.path   

def read_persons_from_file():
    with open(os.path.join(settings.personsFileDirectory, settings.personsFile)) as f:
        for line in f:
            personData = line.split(",")
            wishlistData = personData[2].split(";")
            blacklistData = personData[4].split(";")
            settings.personsList.append(Person.Person(name=personData[0], email=personData[1], wishlist=wishlistData,relationship=personData[3], blacklist=blacklistData))