from pynorare.dataset import NormDataSet
import attr
from pathlib import Path

@attr.s
class Dataset(NormDataSet):
    repos = attr.ib(default=Path('.'))
    id = 'Kiss-1973-EAT'
    
    def download(self):
        self.download_zip(
                'http://vlado.fmf.uni-lj.si/pub/networks/data/dic/eat/EATnew.zip',
                'pajek-eat.zip',
                filename='EATnew.net',
            )

    def map(self, write_file=True):
        sheet = []
        with open(self.raw_dir.joinpath('EATnew.net').as_posix(), 'r', encoding='utf-8') as f:
            in_v, in_e = False, False
            graph, lookup = {}, {}
            for line in f:
                if line.strip().startswith('*Vertices'):
                    in_v = True
                elif line.strip().startswith('*Arcs'):
                    in_e = True
                    in_v = False
                elif in_v:
                    idx, stimulus = line.strip()[:-1].split(' "')
                    lookup[idx] = stimulus
                    lookup['s:'+stimulus] = idx
                    graph[stimulus] = []
                elif in_e:
                    nA, nB, w = line.strip().split()
                    graph[lookup[nA]] += [(lookup[nB], int(w))]

        for stimulus, edges in sorted(graph.items(), key=lambda x: lookup['s:'+x[0]]):
            if 's:'+stimulus in lookup:
                sheet += [{
                    'VertexID': lookup['s:'+stimulus],
                    'Stimulus': stimulus,
                    'DEGREE': len(edges),
                    'WEIGHTED_DEGREE': sum([x[1] for x in edges]),
                    'EDGES': ';'.join([
                        '{0}:{1}'.format(x[0], x[1]) for x in edges])
                    }]
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)


