import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.Analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates,levels,'.',label =("Past measuremnts of relative water level"))
    poly,x1 = polyfit(dates,levels,p)

    x = matplotlib.dates.date2num(dates)
    x_initial = np.linspace(x[0],x[-1],30)
    plt.plot(x_initial,poly(x_initial - x1),label = "Polynomial")
    plt.title(station[0].name)
    plt.ylim(0,max(levels)+1 )
    plt.plot(x_initial,np.ones(30),linewidth=2,label = "Maximum and minimum typical values typical value",color='g')
    plt.xlabel("Date and Time")
    plt.ylabel("Relative Water Level")
    plt.plot(x_initial,np.zeros(30),linewidth=4,color='g')
    plt.legend()
    plt.show()
    


#upper typical range when relative water level = 1
#lower typical range when relaytive water level = 0

def plot_water_levels(station, dates, levels):

    #plot
    plt.plot(dates,levels, label = "$Water Levels$")
    
    #adds lines for typical high and low ranges
    plt.plot([dates[-1], dates[0]], [station.typical_range[0],
                                    station.typical_range[0]], color='brown', label="$Typical Low$")
    plt.plot([dates[-1], dates[0]], [station.typical_range[1],
                                    station.typical_range[1]], color='blue', label="$Typical High$")
    
    #adds labels for axis, title of plot and rotates date labels by 45 degrees
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title("Station: " + station.name)

    #displays plot  
    plt.show(block=False)
    input('press <ENTER> to continue')




