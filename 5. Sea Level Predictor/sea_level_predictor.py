import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header=0)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, c='blue', label='Sea Level Data')

    # Create first line of best fit
    slope,intercept,_,_,_ = linregress(x, y)
    extend_x = x.append(pd.Series(range(x.iloc[-1] + 1, 2051)))
    plt.plot(extend_x, intercept+slope*extend_x, 'r', label='Line of Best Fit (All Data)')

    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    x_new = df[df['Year'] >= 2000]['Year']
    y_new = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']

    slope_new,intercept_new,_,_,_ = linregress(x_new, y_new)
    extend_x_new = x_new.append(pd.Series(range(x_new.iloc[-1] + 1, 2051)))
    plt.plot(extend_x_new, intercept_new+slope_new*extend_x_new, 'g', label='Line of Best Fit (Since 2000)')

    # Add labels and title
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Sea Level (inches)', fontsize=12)
    plt.title('Rise in Sea Level', fontsize=14)
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()