# Population Data Visualizer

## Project Overview
Population Data Visualizer is a Python project that analyzes city population data from a CSV file and displays results using charts.

## Technologies Used
- Python 3
- Pandas
- Matplotlib
- CSV data

## Dataset
The file population.csv contains:
- City
- Year
- Population

The project uses dummy population data for Raipur and Durg.

## Features
- Calculates total population for the latest year
- Identifies the city with the largest population
- Calculates population growth percentage
- Displays a bar chart comparing city populations
- Displays a line chart showing population trends
- Saves charts as PNG images

## Growth Formula
Growth (%) = ((Latest Population - Earliest Population) / Earliest Population) * 100

## How to Run
1. Install the required libraries:
   python -m pip install pandas matplotlib
2. Run the program:
   python main.py

## Output Files
- population_comparison.png
- population_trend.png

## Author
Bhanu Pratap