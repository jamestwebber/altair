"""
Multifeature Scatter Plot
=========================
This example shows how to make a scatter plot with multiple feature encodings.
"""
# category: basic charts

import altair as alt
from vega_datasets import data

iris = data.iris()

chart = alt.Chart(iris).mark_circle().encode(
    alt.X('sepalLength', scale=alt.Scale(zero=False)),
    alt.Y('sepalWidth', scale=alt.Scale(zero=False, padding=1)),
    color='species',
    size='petalWidth'
)
