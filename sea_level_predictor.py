import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color = "blue" , alpha=0.6, label =" Observation")
    

    # Create first line of best fit
    full_reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = full_reg.slope
    intercept_all = full_reg.intercept
    years_full = pd.Series(range(1880, 2051))
    sea_levels_full = slope_all * years_full + intercept_all
    plt.plot(years_full, sea_levels_full, color='red', label='Best Fit (1880–2050)')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    recent_reg = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = recent_reg.slope
    intercept_recent = recent_reg.intercept
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_levels_recent, color='green', linestyle='--', label='Best Fit (2000–2050)')



    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()