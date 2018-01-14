from geopy.distance import vincenty
from datetime import datetime
import smtplib

# defined in kilometers
MAX_DISTANCE = 10

SENDER_GMAIL = "freeeyeout@gmail.com"
SENDER_PWD = "freeeyeout1"

SMTPSERVER = smtplib.SMTP("smtp.gmail.com", 587)
SMTPSERVER.ehlo()
SMTPSERVER.starttls()
SMTPSERVER.ehlo()
SMTPSERVER.login(SENDER_GMAIL, SENDER_PWD)

def distance(user, item):
    '''
    Calculates distance between two coordinates in kilometers.
    Returns -1 if out of bound.
    '''
    d = vincenty(user, item).kilometers
    return d if d > MAX_DISTANCE else -1

def cleanKwargsForItem(kwargs, user):
    '''
    Clean kwarg fields from form for Item
    '''
    del kwargs['csrfmiddlewaretoken']
    kwargs['user'] = user
    kwargs['return_at'] = datetime.strptime(''.join(kwargs['return_at']), '%Y-%m-%dT%H:%M')
    kwargs['lat'] = 123
    kwargs['lon'] = 456

def sendEmail(address, item, loaner):
    msg = 'Your item ' + item + ' has been loaned by ' + loaner + '!!!!!!'

    SMTPSERVER.sendmail(SENDER_GMAIL, address, msg)
