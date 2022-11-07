from pynorare import NoRaRe
from scipy.stats import spearmanr, pearsonr
from matplotlib import pyplot as plt
from tabulate import tabulate
from numpy.polynomial.polynomial import polyfit
import numpy as np
from tqdm import tqdm


def correlate(
        dsA,
        dsB,
        valA,
        valB,
        norare=None,
        filename=None):
    # we need norare, of course
    if not norare:
        raise ValueError('norare must be supplied')
    # the file is either "plot.pdf" or the name we provide
    filename = filename or 'plot.pdf'

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

    # calculate pearson
    p, pr = pearsonr(colA, colB)
    s, sr = spearmanr(colA, colB)

    # tabulate results
    table = [['Test', 'P-Value', 'R-Statistics', 'Items'], 
            ['pearson', p, pr, len(colA)],
            ['spearman', s, sr, len(colA)]]
    print(tabulate(table, headers='firstrow', floatfmt='.4f'))

    # clear the figure
    plt.clf()

    # plot the data
    plt.plot(colA, colB, '.')

    plt.xlabel(valA)
    plt.ylabel(valB)

    # taken from https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
    x, y = np.array(colA), np.array(colB)
    b, m = polyfit(x, y, 1)
    plt.plot(x, b+m*x, '-')
    plt.title(f'{valA} in {dsA} \n{valB} in {dsB}')
    plt.savefig(filename)

    return [len(colA), p, pr, s, sr]


checks = [
        [
            'Scott-2019-Ratings',
            'Cortese-2008-AoA',
            'english_aoa_mean',
            'english_aoa_mean',
            'plot-english-aoa'
            ],
        [
            'Scott-2019-Ratings',
            'Warriner-2013-AffectiveRatings',
            'english_arousal_mean',
            'english_arousal_mean',
            'plot-english-arousal'
            ],
        [
            'Brysbaert-2014-Concreteness',
            'Scott-2019-Ratings',
            'english_concreteness_mean',
            'english_concreteness_mean',
            'plot-english-concreteness'
            ],
        [
            'Scott-2019-Ratings',
            'Warriner-2013-AffectiveRatings',
            'english_dominance_mean',
            'english_dominance_mean',
            'plot-english-dominance'
            ],
        [
            'Scott-2019-Ratings',
            'Warriner-2013-AffectiveRatings',
            'english_valence_mean',
            'english_valence_mean',
            'plot-english-valence'
            ],
        [
            'GonzalezNosti-2014-LexicalDecision',
            'Alonso-2015-AoA',
            'spanish_aoa_mean',
            'spanish_aoa_mean',
            'plot-spanish-aoa'
            ],
        [
            'Cuetos-2011-Frequency',
            'Alonso-2011-OralFrequency',
            'spanish_frequency_log',
            'spanish_frequency_log',
            'plot-spanish-frequency'
            ],
        [
            'Alonso-2016-AoA',
            'Luniewska-2019-299',
            'spanish_aoa_mean',
            'spanish_aoa',
            'plot-spanish-aoa-2'
        ],
        [
            'Cuetos-2011-Frequency',
            'Desrochers-2010-330',
            'spanish_frequency_log',
            'subjective_freq_mean',
            'plot-spanish-frequency-2'
        ],
        [
            'Luniewska-2019-299',
            'Kuperman-2012-AoA',
            'english_aoa',
            'english_aoa_mean',
            'plot-english-aoa-2'
        ],
        [
            'Lynott-2013-400',
            'Lynott-2019-Sensorimotor',
            'olfactory_mean',
            'english_olfactory_mean',
            'plot-english-olfactory'
        ]
            ]

norare = NoRaRe('../')
for dsA, dsB, valA, valB, filename in checks:
    correlate(dsA, dsB, valA, valB, norare=norare, filename=filename)



