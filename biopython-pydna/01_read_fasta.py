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

results
