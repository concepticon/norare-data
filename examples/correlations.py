from pynorare.norare import NoRaRe
from scipy.stats import spearmanr, pearsonr
from matplotlib import pyplot as plt
from tabulate import tabulate
from numpy.polynomial.polynomial import polyfit
import numpy as np
from tqdm import tqdm

norare = NoRaRe('../')

dsA = 'Rzymski-2020-1624'
dsB = 'Desrochers-2009-SubjFrequency'

valA = 'weighted_family_degree'
valB = 'french_subjective_frequency'

# select the concept lists from norare
dsetA = norare.datasets[dsA]
dsetB = norare.datasets[dsB]

# select the relevant columns from the concept list
colA, colB = [], []
dsetB_set = set(dsetB.concepts)
dsetB_concepts = dsetB.concepts
for cid, concept in tqdm(dsetA.concepts.items()):
    if cid in dsetB_set:
        colA += [concept[valA]]
        colB += [dsetB_concepts[cid][valB]]

print('Commons {0}'.format(len(colA)))

# calculate pearson
p, pr = pearsonr(colA, colB)
s, sr = spearmanr(colA, colB)

# tabulate results
table = [['Test', 'P-Value', 'R-Statistics', 'Items'], 
        ['pearson', p, pr, len(colA)],
        ['spearman', s, sr, len(colA)]]
print(tabulate(table, headers='firstrow', floatfmt='.4f'))

# plot the data
plt.plot(colA, colB, '.')

plt.xlabel(valA)
plt.ylabel(valB)

# taken from https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
x, y = np.array(colA), np.array(colB)
b, m = polyfit(x, y, 1)
plt.plot(x, b+m*x, '-')

plt.title(f'{valA} in {dsA} \n{valB} in {dsB}')

plt.savefig('plot-test.pdf')
