# Python third-party modules

Examples and exercises introducing Python libraries for biological sequences, tabular data, plotting, and numerical modelling.

## Folder guide

| Folder | Contents | Start here |
| --- | --- | --- |
| `biopython-pydna/` | Three examples: summarize FASTA sequences and GC content, translate coding-sequence mutations, and simulate a PCR product. Includes a sample FASTA file and a requirements file. | [Biopython and pydna index](biopython-pydna/index.md) |
| `pandas-polars/` | Three examples: filter gene-expression results, summarize replicate measurements, and join gene annotations to experimental results. Includes a requirements file. | [pandas and Polars index](pandas-polars/index.md) |
| `matplotlib-numpy-scipy/` | Plotting and numerical examples, progressing from NumPy arrays and simple plots to ordinary differential equations, microbial growth, batch cultures, chemostats, and fed-batch cultures. Also contains a MATLAB file and a ZIP archive of reactor simulations. | [Browse the scripts](matplotlib-numpy-scipy/) |
| `exercises/` | Short exercises for Biopython, pydna, pandas, and Matplotlib, with supplied checks. Tasks cover DNA translation, restriction cloning into the included pUCmu vector, gene filtering, and growth-curve plotting. | [Exercise instructions](exercises/README.md) |

The `matplotlib-numpy-scipy/` folder has no index file. Begin with [00_matplotlib_numpy_hello_world.py](matplotlib-numpy-scipy/00_matplotlib_numpy_hello_world.py), then follow the numbered scripts.

## Working with the material

Open the example scripts in Spyder or run them with Python in an environment containing the libraries they import. The two indexes above explain the biological questions, code, and expected results for their examples.

For the exercises, follow the [exercise instructions](exercises/README.md), replace the marked placeholders with your code, and run the supplied checks. Keep the included `pUCmu.gb` file beside `pydna_exercise.py`.
