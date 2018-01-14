from geopy.distance import vincenty
from datetime import datetime

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
    kwargs['lat'] = 123
    kwargs['lon'] = 456
