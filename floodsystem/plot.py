import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.Analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates,levels,'.',label =("Past measuremnts of water level"))
    poly,x1 = polyfit(dates,levels,p)
    x = matplotlib.dates.date2num(dates)
    x_initial = np.linspace(x[0],x[-1],30)
    plt.plot(x_initial,poly(x_initial - x1),label = "Polynomial for water level")
    plt.title(station[0].name)
    plt.ylim(0,max(levels)+0.05 )
    plt.axhline(station[0].typical_range[0],label = "High and low typical range")
    plt.axhline(station[0].typical_range[1])
    plt.xlabel("Date and Time")
    plt.ylabel("Relative Water Level")
    plt.legend()
    plt.show()
    


#upper typical range when relative water level = 1
#lower typical range when relaytive water level = 0

def plot_water_levels(station, dates, levels):
    """Takes an input of dates and water levels and plots both on a graph.
    Also shows the typical high and low for the station on the same graph.
    Does not show the graph."""

    # Plot
    plt.plot(dates, levels, label="$water levels$")

    # add lines of typical high and low
    plt.plot([dates[-1], dates[0]], [station.typical_range[0],
                                     station.typical_range[0]], color='g', label="$typical low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1],
                                     station.typical_range[1]], color='r', label="$typical high$")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: " + station.name)

    # Display stuff
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()



