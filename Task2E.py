from floodsystem.stationdata import *
from floodsystem.plot import plot_water_levels
from floodsystem.Flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def run():

    # Build stations
    stations = build_station_list()

    # Update station data
    update_water_levels(stations)
    
    # Get top 5 stations
    stations_at_risk = stations_highest_rel_level(stations, 5)

    # Gather level data for rivers
    dt = 10
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station[0].measure_id,\
        dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)

if __name__=="__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    # Run Task2E
    run()