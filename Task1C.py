from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
stations = build_station_list()
sorted_stations = stations_within_radius(stations, (52.2053, 0.1218),10)
print(sorted_stations)


