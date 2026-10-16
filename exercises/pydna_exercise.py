"""A small pydna cloning exercise. Fill in the function, then run this file."""
from pathlib import Path

from Bio.Restriction import BamHI, HindIII
from pydna.dseqrecord import Dseqrecord
from pydna.readers import read

try:
    here = Path(__file__).resolve().parent
except NameError:
    here = Path.cwd()


# A. clone_fragment
# Clone a linear DNA fragment into pUCmu using HindIII and BamHI.
# The argument is a linear Dseqrecord with exactly one HindIII site
# (AAGCTT), followed by exactly one BamHI site (GGATCC) on its top strand.
# Both sites have flanking DNA, so digestion gives three fragments.
# Return a circular Dseqrecord: the pUCmu backbone containing the insert
# between these sites. Discard the insert's outer flanks and the small
# fragment removed from pUCmu. The vector is read for you below.
#
# Hints:
# - .cut(HindIII, BamHI) returns the restriction fragments.
# - max(fragments, key=len) selects the larger vector backbone.
# - For the supplied inserts, left, insert, right = fragment.cut(...)
#   selects the middle fragment in its original order.
# - Join compatible ends with +, then close the circle with .looped().
def clone_fragment(fragment):
    vector = read(here / 'pUCmu.gb')
    assert vector.seguid() == 'cdseguid=jEg2G-c5DZWICcghJ_xmafqcsTQ', 'checksum does not match.'
    # +++your code here+++
    return





# Provided test helpers: leave these unchanged.
def test(got, expected):
    prefix = ' OK ' if got == expected else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def clone_details(product):
    if product is None:
        return None
    # SEGUID checks the full DNA sequence, allowing circular rotation
    # and reverse complementation. Length and circularity are also checked.
    return len(product), product.circular, product.seguid()


def main():
    print('clone_fragment: 22 bp insert between the restriction sites')
    fragment = Dseqrecord('TTTTTT' 'AAGCTT' 'ACGTCGATGACCTGACGTTAGC' 'GGATCC' 'AAAAAA')
    test(clone_details(clone_fragment(fragment)),
         (1667, True, 'cdseguid=rRXUnVYZ1HRxumS60vhXj9dEfkQ'))

    print('clone_fragment: 15 bp insert between the restriction sites')
    fragment = Dseqrecord('TTTTTT' 'AAGCTT' 'ATGGAATTTGCTTAA' 'GGATCC' 'AAAAAA')
    test(clone_details(clone_fragment(fragment)),
         (1660, True, 'cdseguid=kiu_PDyg-jTT25nZTCHBFJOfHkI'))


if __name__ == '__main__':
    main()
