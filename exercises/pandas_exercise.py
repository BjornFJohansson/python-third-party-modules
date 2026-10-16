"""A small pandas exercise. Fill in the function, then run this file."""
import pandas as pd


# A. significant_genes
# Given a DataFrame with columns 'gene' and 'padj', return a list
# of gene names whose padj is strictly less than 0.05.
# Keep the original row order. All padj values are numeric.
# Hint: filter the rows, select the 'gene' column, then use .tolist().
def significant_genes(genes):
    # +++your code here+++
    return


# Provided test helper: leave this unchanged.
def test(got, expected):
    prefix = ' OK ' if got == expected else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('significant_genes')
    test(significant_genes(pd.DataFrame({
        'gene': ['ERG1', 'ERG11', 'ACT1', 'HSP82'],
        'padj': [0.002, 0.01, 0.8, 0.2],
    })), ['ERG1', 'ERG11'])
    test(significant_genes(pd.DataFrame({
        'gene': ['A', 'B', 'C'], 'padj': [0.05, 0.049, 0.001],
    })), ['B', 'C'])
    test(significant_genes(pd.DataFrame({
        'gene': ['ACT1', 'HSP82'], 'padj': [0.8, 0.2],
    })), [])


if __name__ == '__main__':
    main()
