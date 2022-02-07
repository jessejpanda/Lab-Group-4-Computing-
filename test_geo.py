from unittest.util import sorted_list_difference
from floodsystem.geo import stations_by_distance,stations_within_radius,rivers_with_station,stations_by_river,rivers_by_station_number
from floodsystem.stationdata import build_station_list
#test for funtion used in Task 1B
def test_stations_by_distance():
    """Tests to check that the outputs from funtion stations_by_distance are as expected"""
    stations = build_station_list()
    sorted_stations = stations_by_distance(stations, (52.2053, 0.1218)) 
    assert sorted_stations[0][2] < sorted_stations[1][2]
    for station in sorted_stations:
        assert type(station) is tuple
        assert type(station[0]) is str or "Nonetype"
        assert type(station[1]) is str or "NoneType"
        assert type(station[2]) is float
        assert stations_by_distance(stations, (52.2053, 0.1218))[0:10][0]==('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494)
    i=0    
    for i in range(0,len(sorted_stations)-1):
        assert sorted_stations[i][2]<= sorted_stations[i+1][2]
  


#Test for function used in 1C
def test_stations_within_radius():
    """Tests to check that the outputs from funtion stations_within_radius are as expected"""
    stations = build_station_list()
    sorted_stations = stations_within_radius(stations, (52.2053, 0.1218),10)
    for station in sorted_stations:
        assert type(station) is str
    assert sorted_stations == sorted(sorted_stations)
    assert stations_within_radius(stations, (52.2053, 0.1218),10)[0]== "Bin Brook"
    

#Test for task 1D

#Test for task 1E
def test_rivers_by_station_number():
    """Tests to check that the outputs from funtion rivers_by_station_number are as expected"""
    stations = build_station_list()
    test = rivers_by_station_number(stations, 9)
    for station in test:
        assert type(station) is tuple 
        assert type(station[1]) is int
    i=0
    for i in range(0,len(test)-1):
        assert test[i][1] >= test[i+1][1]



