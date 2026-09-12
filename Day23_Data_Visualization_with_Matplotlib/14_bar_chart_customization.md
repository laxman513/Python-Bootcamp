# Program 14 — Bar Chart Customization

## Objective

Learn how to make bar charts easier to understand.

## Concepts

- Bar width
- Grid
- bar.get_height()
- plt.text()
- Looping through bars

## Important

plt.bar() returns BarContainer containing the bars.

We can loop through the bars:

for bar in bars:

Then get the height:

bar.get_height()

This allows us to display the actual value above each bar.

## Run

python 14_bar_chart_customization.py

## Expected Result

A bar chart with:

- Department labels
- Employee counts
- Grid lines
- Values displayed above bars