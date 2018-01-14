from geopy.distance import vincenty

# defined in kilometers
MAX_DISTANCE = 10

def distance(user, item):
    '''
    Calculates distance between two coordinates in kilometers.
    Returns -1 if out of bound.
    '''
    d = vincenty(user, item).kilometers
    return d if d > MAX_DISTANCE else -1
