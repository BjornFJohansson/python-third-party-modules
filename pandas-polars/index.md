# pandas and Polars for bioinformatics

These libraries are useful whenever bioinformatics data form a **table**, such as genes × measurements, sequence annotations, or sample metadata.

Here are three short, self-contained examples using **example data**. The operations follow the official [pandas](https://pandas.pydata.org/docs/user_guide/groupby.html) and [Polars](https://docs.pola.rs/user-guide/getting-started/) documentation.

The most important data structure in Pandas and Polars is the dataframe (df).

A pandas DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). 

## Running the examples

Install the dependencies:

```bash
conda install pandas polars
```

Run each script from this folder:

```bash
python 01_filter_genes.py
python 02_summarize_replicates.py
python 03_add_annotations.py
```

## 1. Select genes from an RNA-seq results table — pandas

After a differential-expression analysis, select genes with an adjusted p-value below 0.05 and at least a twofold change in either direction.

Script: [01_filter_genes.py](01_filter_genes.py)

```python
import pandas as pd

genes = pd.DataFrame({
    "gene": ["ERG1", "ERG11", "ACT1", "HSP82"],
    "log2FoldChange": [1.8, -1.3, 0.1, 2.1],
    "padj": [0.002, 0.01, 0.8, 0.2],
})

selected = genes[
    (genes["padj"] < 0.05)
    & (genes["log2FoldChange"].abs() >= 1)
]

print(selected)
```

**Result:** `ERG1` and `ERG11` pass both filters. `HSP82` has a large estimated change but fails the adjusted p-value threshold.

These are typical columns in [DESeq2 results](https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html). Here, pandas filters existing statistical results; it does not calculate the differential-expression statistics.

## 2. Summarize measurements across replicates — Polars

Calculate the mean enzyme activity for each strain without writing a loop.

Script: [02_summarize_replicates.py](02_summarize_replicates.py)

```python
import polars as pl

measurements = pl.DataFrame({
    "strain": ["WT", "WT", "mutant", "mutant"],
    "activity": [10.0, 12.0, 18.0, 22.0],
})

summary = (
    measurements
    .group_by("strain")
    .agg(pl.col("activity").mean().alias("mean_activity"))
    .sort("strain")
)

print(summary)
```

**Result:** WT has mean activity **11**, and the mutant has **20**. The same grouping operation works with many strains and replicates. See the [Polars aggregation guide](https://docs.pola.rs/user-guide/expressions/aggregation/).

## 3. Add gene annotations to experimental results — pandas

Combine two tables using a shared gene identifier, even when their rows appear in different orders.

Script: [03_add_annotations.py](03_add_annotations.py)

```python
import pandas as pd

results = pd.DataFrame({
    "gene": ["ERG11", "ACT1", "ERG1"],
    "fold_change": [0.4, 1.1, 3.5],
})

annotations = pd.DataFrame({
    "gene": ["ERG1", "ERG11", "ACT1"],
    "process": ["sterol synthesis", "sterol synthesis", "cytoskeleton"],
})

annotated = results.merge(annotations, on="gene", validate="many_to_one")

print(annotated)
```

**Result:** each measurement receives the annotation belonging to its gene. This is useful when combining experimental output with a separate annotation file.

For real data, replace the `pd.DataFrame(...)` construction with `pd.read_csv("results.tsv", sep="\t")`. [pandas file-reading documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
