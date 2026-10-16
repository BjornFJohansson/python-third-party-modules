# Biopython and pydna for bioinformatics

**Biopython** helps read biological files and analyse sequences. **Pydna** builds on Biopython to 
model double-stranded DNA and laboratory operations such as PCR and cloning.

## 1. Summarize a FASTA file — Biopython

**Question:** What sequences are in my file, how long are they, and what is their GC content?

[01_read_fasta.py](01_read_fasta.py) reads the supplied [sequences.fasta](sequences.fasta). This is useful for an initial inspection before comparing sequences or designing experiments. `SeqIO.parse` handles FASTA records without manually splitting headers and sequence lines.

```python
"""Summarize synthetic DNA records from a FASTA file."""
from pathlib import Path
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

try:
    here = Path(__file__).resolve().parent
except NameError:
    here = Path.cwd()

records = list(SeqIO.parse(here / "sequences.fasta", "fasta"))

results = []
for r in records:
    results.append((r.id, len(r), round(100 * gc_fraction(r.seq), 1)))

# Inspect summary: (sequence ID, length in bp, GC percentage).
```

**Result:** `summary` is `[('gene_A', 15, 26.7), ('gene_B', 12, 58.3)]`: identifier, length in base pairs, and GC percentage. Replace the FASTA file with your own DNA records to apply the same operation.

Documentation: [Biopython sequence input/output](https://biopython.org/docs/latest/Tutorial/chapter_seqio.html) and [GC calculation](https://biopython.org/docs/latest/api/Bio.SeqUtils.html#Bio.SeqUtils.gc_fraction).

## 2. Interpret a coding-sequence mutation — Biopython

**Question:** Does a DNA substitution change an amino acid or introduce a stop codon?

[02_mutation_to_protein.py](02_mutation_to_protein.py) translates three short coding sequences using the standard genetic code.

```python
"""Compare the protein consequences of two synthetic point mutations."""
from Bio.Seq import Seq

reference = Seq("ATGGAATTTGCTTAA")
missense = Seq("ATGGACTTTGCTTAA")  # GAA -> GAC: glutamate -> aspartate.
nonsense = Seq("ATGTAATTTGCTTAA")  # GAA -> TAA: premature stop.

reference_protein = reference.translate()
missense_protein = missense.translate()
nonsense_protein = nonsense.translate()
# Inspect the proteins: MEFA*, MDFA*, M*FA*.
```

**Result:** the reference gives `MEFA*`; the missense variant gives `MDFA*` (E → D at amino acid 2); the nonsense variant gives `M*FA*` (a stop at amino acid 2). `*` marks a stop codon. By default, translation displays codons after a stop; `nonsense.translate(to_stop=True)` gives the predicted truncated sequence `M`.

For real sequences, establish the coding strand, reading frame and appropriate genetic code first. This example demonstrates sequence consequences; it does not predict protein activity.

Documentation: [Biopython translation](https://biopython.org/docs/latest/Tutorial/chapter_seq_objects.html#translation).

## 3. Predict a PCR product — pydna

**Question:** What DNA sequence and product size should these primers produce?

[03_simulate_pcr.py](03_simulate_pcr.py) supplies two primers and an 80 bp linear template. The outer 10 bp flanks lie outside the amplified region. Both primers are written 5′ → 3′; the reverse primer binds the opposite strand.

```python
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
```

**Result:** `product_length` is **60 bp**, including both primer sequences. `product_sequence` contains the amplified DNA; `primer_binding` shows how the primers bind. In the IPython console, use `print(primer_binding)` to display the diagram with line breaks.

This is useful for checking primer orientation and expected product size before planning an experiment. The synthetic template is deliberately small; simulation does not establish amplification specificity in a real genome or guarantee laboratory success.

Documentation: [pydna PCR guide](https://pydna.readthedocs.io/latest/notebooks/PCR.html).

## Why use both?

Biopython can read and analyse your sequence data; pydna can model what happens when you manipulate that DNA. A practical workflow is to read a sequence file, simulate a PCR product, then analyse or export the predicted sequence with Biopython.
