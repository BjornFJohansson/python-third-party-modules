"""Predict PCR sequence and size from a synthetic DNA template."""
from pydna.amplify import pcr
from pydna.dseqrecord import Dseqrecord

# All sequences are written 5' -> 3'; the template shows its top strand.
template = Dseqrecord(
    "TTGACCGTAA"
    "ATGCGTACGTTAGCTAGGCA"
    "CCGATTCGATGACCTAGTCA"
    "GCTACCGATGTTACGGCATC"
    "AACCTGGTTA"
)
fp = "ATGCGTACGTTAGCTAGGCA"
rp = "GATGCCGTAACATCGGTAGC"  # Reverse complement of the right-hand binding site.

product = pcr(fp, rp, template)
product_length = len(product)
product_sequence = str(product.seq)
primer_binding = product.figure()
# Inspect product_length (60 bp), product_sequence, and primer_binding.
