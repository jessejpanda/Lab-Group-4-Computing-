from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
stations = build_station_list()
sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))
ten_closest=sorted_stations[0:10]
ten_furthest=sorted_stations[-10:]
print("The 10 furthest stations are:\n")
for i in ten_furthest:
    print(i)
    print("")

print("\nThe 10 closest stations are:\n")
for i in ten_closest:
    print(i)
    print("")