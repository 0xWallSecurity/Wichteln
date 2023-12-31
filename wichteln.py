import helpers.settings as settings
import helpers.helpers as helpers
import random
import smtplib
from email.mime.text import MIMEText

def wichteln():
    wichtelnMapping = {} # email(gifter) -> email(receiver)
    receiverList = settings.personsList.copy()
    for person in settings.personsList:
        if settings.DEBUG:
            print(f"looking for mapping for {person.email}.")
        foundMatch = False
        while not foundMatch:
            randomChoice = random.choice(receiverList)
            if len(receiverList) == 1 and (randomChoice == person or randomChoice.email in person.blacklist or randomChoice.relationship in person.blacklist):
                print(f"endless loop detected: {person.email} to {randomChoice.email}. Aborting.")
                return {}
            if randomChoice != person and randomChoice.email not in person.blacklist and randomChoice.relationship not in person.blacklist:
                if settings.DEBUG:
                    print(f"found mapping {person.email} to {randomChoice.email}.")
                wichtelnMapping[person] = randomChoice
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

def send_mails(mapping):
    if mapping:
        for person in mapping:
            mappedPerson = mapping.get(person)
            recipient = person.email
            wishlist = f""
            for wish in mappedPerson.wishlist:
                wishlist = wishlist + f"{wish}\n"
            body = f"""
Ho Ho Ho {person.name},

In sternenklarer, dunkler Nacht,
Ein Päckchen, das für dich erwacht.
Geheimnisvoll und sanft verpackt,
Die Vorfreude leise klingend lacht.

Ein Rätsel, wer es wohl gesandt,
In zarter Hülle, bunt umsäumt.
Ein Hauch von Zauber in der Luft,
Ein Lächeln, das die Stille rühmt.

In diesem Sinne: Bitte suche dir aus den unten stehenden Wünschen einen (oder gegebenenfalls auch mehrere) aus.
Bedenke dabei bitte unser festgelegtes Budget von maximal 30€.

---
{wishlist}---

Bis zum 26. - Santa
"""
            if settings.DEBUG:
                print(f"{settings.sender} sends email to {recipient} / {person.name}.")
                print(f"{mappedPerson.name} has wishlist: {wishlist}")

            msg = MIMEText(body)
            msg['Subject'] = settings.subject
            msg['From'] = settings.sender
            msg['To'] = recipient
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(settings.senderEmail, settings.password)
                smtp_server.sendmail(settings.sender, recipient, msg.as_string())
                print("Message sent!")

settings.init()
helpers.read_persons_from_file()
mapping = wichteln()
send_mails(mapping)
