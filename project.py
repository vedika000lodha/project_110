import csv
import pandas as pd 
import statistics 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

population_std_dev = statistics.stdev(data)
print("population mean : ", population_mean)
print("population standard deviation : ", population_std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution : ", mean)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.8], mode = "lines", name = "mean"))
    fig.show()

setup()