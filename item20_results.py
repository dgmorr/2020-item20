# Python code to aggregate results

items = [
    "reactor",
    "trainwash",
    "frizzle",
    "lion",
    "banana",
    "ice",
    "brixel",
    "quad",
    "sonic",
    "fish",
    "eyes"
]
axes = [
    ("introverted", "extroverted"),
    ("blessed", "cursed"),
    ("intellectual", "physical"),
    ("refined", "janky"),
    ("modest", "flamboyant"),
    ("blue collar", "ivory tower"),
    ("artistic", "scientific"),
    ("ludicrous", "sensible"),
    ("trustworthy", "suspicious"),
    ("charming", "awkward")
]

n_items = len(items)
n_axes = len(axes)

import numpy as np

csv_path = ""
f = open(csv_path, 'r')
f.readline() # ignore header
datarows = []
n_responses = len(datarows)
for line in f:
    vals = [int(n) for n in line.split(',')[1:]]
    datarows.append(vals)
data = np.array(datarows).transpose()
itemized_data = {}
for i in range(n_items):
    item_stats_raw = data[i*n_axes:(i+1)*n_axes]
    item_stats = agg(item_stats_raw)
    itemized_data[items[i]] = item_stats

def agg(item_stats_raw):
    # Expects a 2d numpy array with n_axes rows and n_responses columns
    # Reduces to a mapping from each axis to a single representative float
    item_stats = {}
    for i in range(n_axes):
        item_stats[axes[i]] = 5.
    
    
