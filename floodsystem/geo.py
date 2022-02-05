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
    geo.py to calclate the distance from the station and the coordiante p."""
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
    return sorted_by_key(name_distance,0)

"""This function finds al stations wityhion a 10km radius"""

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
    

