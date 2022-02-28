from floodsystem.Flood import stations_level_over_threshold,stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

#Test for Task 2B
def test_stations_level_over_threshold():
     """Tests to check that the outputs from funtion "stations_level_over_threshold" are as expected"""
     stations = build_station_list()
     update_water_levels(stations)
     list_of_over = []
     for station_tuple in stations_level_over_threshold(stations, 0.8):
         list_of_over.append(station_tuple)
     
     for i in range(0,len(list_of_over)-1):
         assert list_of_over[i][1]>=list_of_over[i+1][1]
         assert type(list_of_over[i]) is tuple
         assert type(list_of_over[i][0].name) is str
         assert type(list_of_over[i][1]) is float
     test_stations_level_over_threshold         
     
#Test for task 2C
def test_stations_highest_rel_level():
     """Tests to check that the outputs from funtion "test_stations_highest_rel_level" are as expected"""
     stations = build_station_list()
     update_water_levels(stations)
     list_of_over = []
     for station_tuple in stations_highest_rel_level(stations, 10):
         list_of_over.append(station_tuple)
     
     assert len(list_of_over)==10
     for i in range(0,len(list_of_over)-1):
         assert list_of_over[i][1]>=list_of_over[i+1][1]
         assert type(list_of_over[i]) is tuple
         assert type(list_of_over[i][0].name) is str
         assert type(list_of_over[i][1]) is float
         



         #yml comment
