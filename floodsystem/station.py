# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    #Task 1F
    def typical_range_consistent(self):
        """This fucntion takes monitoring station attributes(self) as the arguement and assign "True" to those with 
        consistent data and "False" otherwise."""
        if self.typical_range ==  None:
            return False
        elif self.typical_range[0] - self.typical_range[1] > 0:
            return False

        return True
    #Method for Task 2B
    def relative_water_level(self):
        if not self.typical_range_consistent():
            return None
        elif self.latest_level == None:
            return None
        else:
            range_of_tr = self.typical_range[1] - self.typical_range[0]
            ratio = (self.latest_level - self.typical_range[0])/range_of_tr 
            return ratio


#Task 1F    
def inconsistent_typical_range_stations(stations):
    """This function takes the list of station objets as the argument and returns a list of monitoring stations which 
    produce inconsistent data."""
    excluded_stations = [] 
    for station in stations:
        if not station.typical_range_consistent():
            excluded_stations.append(station)       
    return excluded_stations
        
    



        

