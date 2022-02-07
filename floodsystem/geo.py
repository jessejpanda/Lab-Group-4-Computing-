# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key
from haversine import haversine

#Task 1B
def stations_by_distance(stations, p):
    """A function which takes the list of stations and then uses the haversine formula imported from 
    geo.py to calclate the distance from the station and the coordiante p. The function will return the ten furtherst and ten closest monitoring stations to the coordiante 
    C in the form of (station,town,distance from C). """
    distance = []
    stationname = []
    towns = []
    name_distance = []
    for station in stations:
        towns.append(station.town)
        stationname.append(station.name)
        distance.append(haversine(station.coord,p))
    i=0
    while i<len(stationname):
        name_distance.append((stationname[i],towns[i],distance[i]))
        i+=1
    return sorted_by_key((name_distance),2)

#Task 1C
def stations_within_radius(stations, centre, r):
    """The function which takes a point and a distance and returns all the monitoring stations which are within the distance from that point in alphabetical order. """
    distance = []
    stationname = []
    name_distance = []
    for station in stations:
        stationname.append(station.name)
        distance.append(haversine(station.coord,centre))
    i=0
    while i<len(stationname):
        if distance[i]<r:
            name_distance.append(stationname[i])
        i+=1
    return sorted(name_distance)


#Task 1D

def rivers_with_station(stations):
    return set([station.river for station in stations])

def stations_by_river(stations):
    river_names = {}
    for station in stations:
        if station.river in river_names:
            river_names[station.river].append(station.name)
        else :
            river_names[station.river] = [station.name]
    return river_names
    
#Task 1E
#Sort rivers into order of monitoring stations on that river then print the top N  If there are some with the same valueas the Nth river then these should also be shown\
def rivers_by_station_number(stations, N):
    """This funtion takes a number (N) as an argument. The function will return a tuple of river and the number of monitoring stations on that river sorted from high to low, but it
    will only show the top N rivers."""
    rivers = stations_by_river(stations)
    top_rivers = []
    stations_per_river = []
    for river in rivers:
        stations_per_river.append(len(rivers[river]))
    sorted_stations_per_river = sorted(stations_per_river)
    sorted_stations_per_river.reverse()
    min_stations = sorted_stations_per_river[N-1]
    for river in rivers:
        if len(rivers[river])>= min_stations:
            top_rivers.append((river,len(rivers[river])))
    final_rivers = sorted_by_key(top_rivers,1)
    final_rivers.reverse()
    return(final_rivers)



        


    
