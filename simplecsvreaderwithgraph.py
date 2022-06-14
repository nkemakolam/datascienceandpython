# install and import all the datascience python library using pip for installation and import to your scriot file
import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
# defining the  csv file you want to work on and refereningf the path where it is stored
# best to have it in the root working directory where your script lives
str_filename = 'mountain.csv'
fh = open(str_filename)
#using the csv lib to read and separate header from the file content
csv_reader = csv.reader(fh)
csv_header = next(csv_reader)
# printing the  out put of the header to see if you are on track
print(csv_header)

# After reading the headers bow is time to use pandas to read the csv and sellecting the filed or columns you are interested in and skiping the header
df_output = pd.read_csv(str_filename,header=None,skiprows=1,names=csv_header)
print(df_output)

# function to plot the graph using numberic axis columns in the csv 
def plotter():
    df_output.Metres.plot()
    plt.xlabel('Sample number')
    plt.ylabel('output value feet')
    plt.show()

print('getting ready to plot')
graph = plotter()
print(graph)