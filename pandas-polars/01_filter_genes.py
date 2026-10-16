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
