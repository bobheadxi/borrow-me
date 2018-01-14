from geopy.distance import vincenty
from datetime import datetime
from borrow_me.settings import SMTPSERVER, SENDER_GMAIL

# defined in kilometers
MAX_DISTANCE = 10

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

def sendLoanedEmail(address, item, loaner):
    '''
    Send email notifying loaner of loan
    '''
    msg = 'Your item ' + item + ' has been loaned by ' + loaner.username + '!!!!!!\n' + 'You can contact the loaner at ' + loaner.email + '.\n For your contribution, you have gained 5 karma!'  
    _sendEmail(address, msg)

def sendLoanerEmail(address, item, due):
    msg = 'You have borrowed ' + item + ' - it is due on ' + due.isoformat()
    _sendEmail(address, msg)

def sendReturnedEmail(address, item, loaner):
    msg = 'Your item ' + item + ' has been returned by ' + loaner.username + '!!!!!!\n' + 'You can contact the loaner at ' + loaner.email
    _sendEmail(address, msg)

def _sendEmail(address, msg):
    SMTPSERVER.sendmail(SENDER_GMAIL, address, msg)
