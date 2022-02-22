from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
stations = build_station_list()
update_water_levels(stations)
for station_tuple in stations_highest_rel_level(stations, 10):
    print(station_tuple[0].name, station_tuple[1])
    