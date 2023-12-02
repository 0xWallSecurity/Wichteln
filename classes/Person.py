class Person:
    """ Simple class do define a member of the game """

    def __init__(self, name, email, wishlist, relationship, blacklist):
        self.name = name
        self.email = email
        self.wishlist = wishlist
        self.relationship = relationship
        self.blacklist = blacklist # defines other persons that this person should not be able to gift