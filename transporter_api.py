# conding: utf-8

# dependency: arrow package (https://arrow.readthedocs.io/en/latest/) for time management
# stop type : string
# line type : string
# times type : list of Arrow objects


def find_nearby_stops(longitude, lattitude):
    """ Find the stops near a given location

        @param longitude of the point of interest
        @param lattitude of the point of interest

        @return list of stops (possibly sorted from closest to fathest)
    """
    raise NotImplementedError()

def get_lines():
    """ Get all the lines in this newtork

        @return list of dictionaries; the dictionaries should have at least the
            following entries : name, terminuses (array)
            the name is either a string or an integer or a Float that can uniquely
            identify the line
    """
    raise NotImplementedError()

def get_lines_at_stop(stop):
    """ Get all the lines passing at the given stop

        @param stop identifier of the stop
        
        @return list of line names
    """
    raise NotImplementedError()

def get_times(stop, line, direction):
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
    raise NotImplementedError()