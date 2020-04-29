from pynorare.norare import NoRaRe
from scipy.stats import spearmanr, pearsonr
from matplotlib import pyplot as plt
from tabulate import tabulate
from numpy.polynomial.polynomial import polyfit
import numpy as np

norare = NoRaRe('../')

dsA = 'Engelthaler-2018-Humor'
dsB = 'Desrochers-2009-SubjFrequency'

valA = 'ENGLISH_HUMOR_MEAN'
valB = 'FRENCH_SUBJECTIVE_FREQUENCY'

colA = norare.get_columns(
        dsA,
        'CONCEPTICON_ID',
        valA, dicts=False)
colB = norare.get_columns(
        dsB,
        'CONCEPTICON_ID',
        valB, dicts=False)

# we create the set() data type
cidA, cidB = {row[0] for row in colA}, {
        row[0] for row in colB}

# we can now take the intersection
common = sorted(cidA.intersection(cidB))
listA, listB = [row[1] for row in colA if row[0] in common], [
        row[1] for row in colB if row[0] in common]

# calculate pearson
p, pr = pearsonr(listA, listB)
s, sr = spearmanr(listA, listB)

# tabulate results
table = [['Test', 'P-Value', 'R-Statistics', 'Items'], 
        ['pearson', p, pr, len(listA)],
        ['spearman', s, sr, len(listA)]]
print(tabulate(table, headers='firstrow', floatfmt='.4f'))

# plot the data
plt.plot(listA, listB, '.')

plt.xlabel(valA)
plt.ylabel(valB)

# taken from https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
x, y = np.array(listA), np.array(listB)
b, m = polyfit(x, y, 1)
plt.plot(x, b+m*x, '-')

plt.title(f'{valA} in {dsA} \n{valB} in {dsB}')

plt.savefig('plot-test.pdf')
