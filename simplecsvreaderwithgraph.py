import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
str_filename = 'mountain.csv'
fh = open(str_filename)
csv_reader = csv.reader(fh)
csv_header = next(csv_reader)
print(csv_header)
# After reading the headers bow is time to use pandas to read the csv

df_output = pd.read_csv(str_filename,header=None,skiprows=1,names=csv_header)
print(df_output)

# function to pot the graph using numberic axis
def plotter():
    df_output.Metres.plot()
    plt.xlabel('Sample number')
    plt.ylabel('output value feet')
    plt.show()

print('getting ready to plot')
graph = plotter()
print(graph)