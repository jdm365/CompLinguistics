import argparse
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np


def get_ranks_and_frequencies(infile):
    """Produces a list of rank, frequency pairs for each word in a text file
    :param infile: a text file
    :return: a list containing rank, frequency pairs for each word
    """
    with open(infile) as f:
        contents = f.read()
    c = Counter(contents.split())
    # TODO: create a list called ranks_and_frequencies that stores (rank,
    # frequency) pairs for each word in the file

    ## Sort key, value by counts.
    ranks_and_frequencies = sorted(c.items(), key=lambda x: x[1], reverse=True)
    return ranks_and_frequencies


def plot(infile):
    """
    Plots rank and frequency pairs to demonstrate Zipf's Law
    :param infile: a text file
    :return: None, produces a matplotlib plot
    """
    ranks_and_frequencies = get_ranks_and_frequencies(infile)

    # TODO: use the (rank, frequency) pairs to plot the data
    # and use a log scale on both axes
    # You will display the plot using plt.show(), which is already written
    sorted_counts = np.log([x[1] for x in ranks_and_frequencies])
    ranks         = list(range(len(sorted_counts)))

    fig, ax = plt.subplots()
    plt.plot(ranks, sorted_counts)
    plt.title('Word count distribution')
    ax.set_xlabel('Frequency Rank')
    ax.set_ylabel('Number of Occurences (log-scale)')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Constructs a curve '
                                                 'demonstrating Zipf\'s Law '
                                                 'by plotting a rank, '
                                                 'frequency plot.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()
    plot(args.path)
