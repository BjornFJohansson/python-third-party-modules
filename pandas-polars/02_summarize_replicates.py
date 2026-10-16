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
