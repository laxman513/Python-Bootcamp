# Program 13 — Multiple Bar Chart

## Objective

Compare two datasets for the same categories.

## Concepts

- NumPy arange()
- Bar positions
- Bar width
- Multiple plt.bar()
- plt.xticks()
- legend()

## Important

We use NumPy to calculate the positions of the bars.

x = np.arange(len(departments))

The two groups are shifted slightly left and right so they appear side-by-side.

## Run

python 13_multiple_bar_chart.py

## Expected Result

Each department should contain two bars:

- 2025
- 2026