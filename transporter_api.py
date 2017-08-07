# conding: utf-8

#TODO: define the type for a stop, a line, and times

""" Find the stops near a given location

    @param longitude of the point of interest
    @param lattitude of the point of interest

    @return list of stops (possibly sorted from closest to fathest)
"""
def find_nearby_stops(longitude, lattitude):
    raise NotImplementedError()

""" Get all the lines in this newtork

    @return list of dictionaries; the dictionaries should have at least the
        following entries : name, terminuses (array)
        the name is either a string or an integer or a Float that can uniquely
        identify the line
"""
def get_lines():
    raise NotImplementedError()

""" Get all the lines passing at the given stop

    @param stop identifier of the stop
    
    @return list of line names
"""
def get_lines_at_stop(stop):
    raise NotImplementedError()

""" Get the time when the bus is to pass at the stop

    @param stop identifier of the stop
    @param line the line we want to get on
    @param direction where we are headed (stop identifier) may be any stop
        between current stop and the desired terminus
    @param scheduled (false by default) if true, return theoretic schedule,
        instead of real time information
    
    @return list of times
        the number of times returned depends on the underlying API and could
        contain times in the past (for all times in the day)
"""
def get_times(stop, line, direction):
    raise NotImplementedError()