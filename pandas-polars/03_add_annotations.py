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
