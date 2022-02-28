from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
stations = build_station_list()
update_water_levels(stations)
for station_tuple in stations_level_over_threshold(stations, 0.8):
    print(station_tuple[0].name, station_tuple[1])
    


    

    