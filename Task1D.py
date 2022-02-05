from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers = rivers_with_station(stations)
r = sorted(rivers)

print(len(r))
print(r[:10])

station_names = stations_by_river(stations)

aire_stations = sorted(station_names['River Aire'])
cam_stations = sorted(station_names['River Cam'])
thames_stations = sorted(station_names['River Thames'])

print(aire_stations)
print('\n')
print(cam_stations)
print('\n')
print(thames_stations)
