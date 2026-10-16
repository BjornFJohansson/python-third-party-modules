"""A small Biopython exercise. Fill in the function, then run this file."""
from Bio.Seq import Seq


# A. translate_dna
# Given a DNA coding strand written 5' -> 3', return the protein
# as a plain string. Stop at the first stop codon and omit '*'.
# Inputs contain complete codons and use the standard genetic code.
# For example, 'ATGGAATAA' gives 'ME'.
# Hint: create a Seq, use .translate(to_stop=True), then str().
def translate_dna(dna):
    # +++your code here+++
    return


# Provided test helper: leave this unchanged.
def test(got, expected):
    prefix = ' OK ' if got == expected else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('translate_dna')
    test(translate_dna('ATGGAATTTGCTTAA'), 'MEFA')
    test(translate_dna('ATGTAATTTGCTTAA'), 'M')
    test(translate_dna('ATGGCT'), 'MA')


if __name__ == '__main__':
    main()
