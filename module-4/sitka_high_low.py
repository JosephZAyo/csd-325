# Joseph Ayo 
# 11/10/24
# Module 4.3 Assignment
# This program displays the daily temperature highs and lows using data
# from a given document and utilizing matplotlib to plot the graph.


import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

# Function to plot temperatures
def plot_temperatures(dates, temperatures, color, highorlow):
    # Plot the temperatures
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)
    
    # Format plot
    plt.title(f"Daily {highorlow} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(f"Temperature (°F) - {highorlow}", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    # Show the plot
    plt.show()

# Read the CSV file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

# Main program loop
def main():
    while True:
        print("\nSelect an option:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        # Get user input
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Plot high temperatures
            plot_temperatures(dates, highs, 'red', 'High')
        elif choice == '2':
            # Plot low temperatures
            plot_temperatures(dates, lows, 'blue', 'Low')
        elif choice == '3':
            # Exit the program
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
main()