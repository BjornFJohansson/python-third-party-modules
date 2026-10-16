# Third-party module exercises

One small exercise per module, following the function-and-tests style of
`google-python-exercises/basic`. Each should take only a few lines to solve.

| File | Task |
| --- | --- |
| `pydna_exercise.py` | Clone a linear fragment into pUCmu with HindIII and BamHI. |
| `biopython_exercise.py` | Translate DNA up to the first stop codon. |
| `pandas_exercise.py` | Select gene names using an adjusted p-value cutoff. |
| `matplotlib_exercise.py` | Draw and label a growth curve. |

Open an exercise, replace `# +++your code here+++` and the placeholder `return`
with your solution, then run the file. For example, from this folder:

```bash
python biopython_exercise.py
```

The provided tests print `OK` for correct results and `X` otherwise. All checks
initially print `X` because the functions are unfinished. Leave the test code
unchanged. The matplotlib exercise also displays your plots when run with a
graphical backend (for example in Spyder). The pydna exercise reads the included `pUCmu.gb` file; keep it beside the script.
No sequence downloads are needed.


The pydna function takes a linear `Dseqrecord` and returns the circular
recombinant plasmid. Its hints cover digestion, selecting the backbone and
insert, ligation, and circularization. The checks verify sequence identity,
length, and circularity for two short synthetic inserts.

`pUCmu.gb` is the 1,669 bp circular cloning vector identified as LMBP 9329,
with checksum `cdseguid=jEg2G-c5DZWICcghJ_xmafqcsTQ`.
The exact local copy was located using Recoll inside
`2020-11-24_test_BMA20_extra.zip`, archive member
`2020-11-24_test_BMA20_extra/empty_exams/Carla_Filipa_Carona_De_Sousa_a80689/pUCmu.gb`.
