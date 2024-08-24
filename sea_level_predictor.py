import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot(): 
    df = pd.read_csv('epa-sea-level.csv')
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c=df['Year'], cmap='viridis')
    
    # Crear primera línea de mejor ajuste
    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xA = np.arange(df['Year'].min(),2050,1)
    yA = xA*lineA.slope + lineA.intercept
    
    plt.plot(xA,yA, color='orange')
    
    df_recent = df[df['Year'] >= 2000]
    
    lineB = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    xB = np.arange(2000,2050,1)
    yB = xB*lineB.slope + lineB.intercept
    
    plt.plot(xB,yB, color='red')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.colorbar(label='Year')
            
    plt.savefig('sea_level_plot.png')
    return plt.gca()
