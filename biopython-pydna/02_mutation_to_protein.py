"""Compare the protein consequences of two synthetic point mutations."""
from Bio.Seq import Seq

reference = Seq("ATGGAATTTGCTTAA")
missense = Seq("ATGGACTTTGCTTAA")  # GAA -> GAC: glutamate -> aspartate.
nonsense = Seq("ATGTAATTTGCTTAA")  # GAA -> TAA: premature stop.

reference_protein = reference.translate()
missense_protein = missense.translate()
nonsense_protein = nonsense.translate()
# Inspect the proteins: MEFA*, MDFA*, M*FA*.
