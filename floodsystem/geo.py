# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
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

