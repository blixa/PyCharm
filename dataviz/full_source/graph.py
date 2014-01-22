"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter
import csv
import matplotlib.pyplot
import numpy.numarray as na
import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """visualize by day/week"""
    # grab our parsed data that we parsed earlier
    parsed_data = parse.parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in parsed_data)

    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                 counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with that y-axis data, assign it to a matplotlib plot instance
    matplotlib.pyplot.plot(data_list)

    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    matplotlib.pyplot.xticks(range(len(day_tuple)), day_tuple)

    # show the plot!
    matplotlib.pyplot.show()

def visualize_type():
    parsed_data = parse.parse(MY_FILE, ",")
    counter = Counter(item["Category"] for item in parsed_data)
    category_tuple = tuple(counter.keys())
    xlocations = na.array(range(len(category_tuple))) + 0.5
    matplotlib.pyplot.bar(xlocations, counter.values())
    matplotlib.pyplot.xticks(xlocations, category_tuple, rotation=90)
    matplotlib.pyplot.subplots_adjust(bottom=0.4)
    matplotlib.pyplot.rcParams["figure.figsize"]= 12,8
    matplotlib.pyplot.show()



def main():
    #visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()