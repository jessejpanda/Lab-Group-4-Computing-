from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations
stations = build_station_list()
excluded_stations = inconsistent_typical_range_stations(stations)
excluded_stations_and_names = []
for station in excluded_stations:
    excluded_stations_and_names.append(station.name)
inconsistent = sorted(excluded_stations_and_names)

print(inconsistent)
