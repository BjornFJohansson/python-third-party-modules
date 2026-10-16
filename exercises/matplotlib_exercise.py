"""A small matplotlib exercise. Fill in the function, then run this file."""
import matplotlib.pyplot as plt


# A. growth_plot
# Given equally long, non-empty lists of times and optical densities,
# create a figure and axes using plt.subplots(). Plot densities against
# times as one line. Label the x axis 'Time (h)' and the y axis 'OD600'.
# Return the axes object (ax). Do not call plt.show() inside the function.
# Hint: use ax.plot(), ax.set_xlabel(), and ax.set_ylabel().
def growth_plot(times, densities):
    # +++your code here+++
    return


# Provided test helper: leave this unchanged.
def test(got, expected):
    prefix = ' OK ' if got == expected else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Summarize the returned axes so the tests can compare plain Python values.
def plot_details(ax):
    if ax is None:
        return None
    return (
        [(list(line.get_xdata()), list(line.get_ydata()))
         for line in ax.get_lines()],
        ax.get_xlabel(), ax.get_ylabel(),
    )


def main():
    print('growth_plot')
    test(plot_details(growth_plot([0, 1, 2], [0.1, 0.2, 0.4])),
         ([([0, 1, 2], [0.1, 0.2, 0.4])], 'Time (h)', 'OD600'))
    test(plot_details(growth_plot([0, 2], [0.05, 0.3])),
         ([([0, 2], [0.05, 0.3])], 'Time (h)', 'OD600'))
    plt.show()


if __name__ == '__main__':
    main()
